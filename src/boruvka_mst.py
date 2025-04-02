from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure for tracking connected components.
    """
    def __init__(self, vertices: int):
        """
        Initialize disjoint set with given number of vertices.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item: int) -> int:
        """
        Find the root of a vertex with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x: int, y: int) -> bool:
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def boruvka_mst(num_vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree.
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is (u, v, weight)
    :return: List of edges in the Minimum Spanning Tree
    
    Time Complexity: O(E log V)
    Space Complexity: O(V + E)
    """
    # Validate input
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        return []
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Create disjoint set
    ds = DisjointSet(num_vertices)
    
    # Result MST
    mst = []
    
    # Track the number of sets (components)
    num_sets = num_vertices
    
    while num_sets > 1:
        # Store cheapest edges for each set
        cheapest = [None] * num_vertices
        
        # Find cheapest edge for each component
        for u, v, weight in edges:
            set_u = ds.find(u)
            set_v = ds.find(v)
            
            # Skip if in same set
            if set_u == set_v:
                continue
            
            # Update cheapest edge for each set
            if (cheapest[set_u] is None or 
                weight < cheapest[set_u][2]):
                cheapest[set_u] = (u, v, weight)
            
            if (cheapest[set_v] is None or 
                weight < cheapest[set_v][2]):
                cheapest[set_v] = (u, v, weight)
        
        # Track if any edge was added in this iteration
        edge_added = False
        
        # Add selected cheapest edges to MST
        for cheap_edge in cheapest:
            if cheap_edge is not None:
                u, v, weight = cheap_edge
                
                # Try to union the sets
                if ds.union(u, v):
                    mst.append((u, v, weight))
                    num_sets -= 1
                    edge_added = True
        
        # If no edge was added, break to prevent infinite loop
        if not edge_added:
            break
    
    return mst