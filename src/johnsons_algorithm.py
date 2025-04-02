import heapq
from typing import List, Dict, Optional, Tuple

def johnsons_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm for finding all-pairs shortest paths in a weighted graph.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list representation of the graph.
                                                  Key is the source vertex, 
                                                  Value is a list of (destination, weight) tuples.
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: A dictionary of shortest paths between all vertex pairs,
                                             or None if a negative cycle is detected.
    
    Raises:
        ValueError: If the graph is empty or not a valid graph representation.
    """
    # Validate input graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Identify all vertices
    vertices = set(graph.keys()).union(
        set(v for edges in graph.values() for v, _ in edges)
    )
    
    # Add a dummy source vertex to run Bellman-Ford
    augmented_graph = graph.copy()
    dummy_vertex = max(vertices) + 1
    augmented_graph[dummy_vertex] = [(v, 0) for v in vertices]
    
    # Step 1: Reweight the graph using Bellman-Ford
    def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Optional[Dict[int, int]]:
        """
        Bellman-Ford algorithm to detect negative cycles and compute vertex potentials.
        
        Args:
            graph (Dict[int, List[Tuple[int, int]]]): Graph representation
            source (int): Source vertex for the shortest path computation
        
        Returns:
            Optional[Dict[int, int]]: Vertex potentials or None if negative cycle detected
        """
        # Initialize distances
        distances = {v: float('inf') for v in vertices}
        distances[source] = 0
        
        # Relax edges |V| - 1 times
        for _ in range(len(vertices) - 1):
            updated = False
            for u in vertices:
                for v, weight in graph.get(u, []):
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        updated = True
            if not updated:
                break
        
        # Check for negative cycles
        for u in vertices:
            for v, weight in graph.get(u, []):
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    return None  # Negative cycle detected
        
        return distances
    
    # Compute vertex potentials
    h = bellman_ford(augmented_graph, dummy_vertex)
    if h is None:
        return None  # Negative cycle detected
    
    # Step 2: Reweight the graph
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for v, weight in graph[u]:
            # Reweight edge: w'(u, v) = w(u, v) + h(u) - h(v)
            reweighted_weight = weight + h[u] - h[v]
            reweighted_graph[u].append((v, reweighted_weight))
    
    # Step 3: Compute shortest paths using Dijkstra's algorithm for each vertex
    shortest_paths = {}
    for source in vertices:
        # Dijkstra's algorithm
        dist = {v: float('inf') for v in vertices}
        dist[source] = 0
        pq = [(0, source)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # Skip if we've found a shorter path
            if current_dist > dist[u]:
                continue
            
            for v, weight in reweighted_graph.get(u, []):
                distance = current_dist + weight
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        # Adjust distances back to original weights
        shortest_paths[source] = {
            v: (dist[v] - h[source] + h[v]) if dist[v] != float('inf') else float('inf')
            for v in vertices
        }
    
    return shortest_paths