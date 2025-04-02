import heapq
from typing import List, Dict, Optional, Tuple
import math

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
    
    # Special case for single vertex graph
    if len(vertices) == 1:
        return {list(vertices)[0]: {list(vertices)[0]: 0}}
    
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
    
    # Detect negative cycle explicit case
    if dummy_vertex in graph and len(graph[dummy_vertex]) > 0:
        return None
    
    # Step 2: Compute all-pairs shortest paths
    shortest_paths = {}
    for source in vertices:
        # Dijkstra's algorithm for each source
        dist = {v: float('inf') for v in vertices}
        dist[source] = 0
        prev = {v: None for v in vertices}
        pq = [(0, source)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # Skip if we've found a shorter path
            if current_dist > dist[u]:
                continue
            
            # Explore neighbors
            for v, weight in graph.get(u, []):
                # Compute alternative path distance 
                alternative_dist = dist[u] + weight
                
                if alternative_dist < dist[v]:
                    dist[v] = alternative_dist
                    prev[v] = u
                    heapq.heappush(pq, (alternative_dist, v))
        
        # Compute paths from source
        paths_from_source = {}
        for v in vertices:
            if v == source:
                paths_from_source[v] = 0
            elif dist[v] == float('inf'):
                paths_from_source[v] = float('inf')
            else:
                paths_from_source[v] = dist[v]
        
        shortest_paths[source] = paths_from_source
    
    return shortest_paths