import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set (Union-Find) data structure."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union of sets
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Multiple unions
    ds.union(2, 3)
    ds.union(3, 4)
    
    assert ds.find(2) == ds.find(3)
    assert ds.find(2) == ds.find(4)
    assert ds.find(0) != ds.find(2)

def test_boruvka_mst_basic():
    """Test Boruvka's algorithm with a simple graph."""
    # Graph with 4 vertices
    edges = [
        (0, 1, 10),  # edge between 0 and 1 with weight 10
        (0, 2, 6),   # edge between 0 and 2 with weight 6
        (0, 3, 5),   # edge between 0 and 3 with weight 5
        (1, 3, 15),  # edge between 1 and 3 with weight 15
        (2, 3, 4)    # edge between 2 and 3 with weight 4
    ]
    
    mst = boruvka_mst(4, edges)
    
    # Expected total weight of MST is 15 (5 + 4 + 6)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 15
    
    # MST should have 3 edges (n-1 where n is number of vertices)
    assert len(mst) == 3

def test_boruvka_mst_disconnected():
    """Test Boruvka's algorithm with a disconnected graph."""
    edges = [
        (0, 1, 10),  # component 1
        (2, 3, 15)   # component 2
    ]
    
    mst = boruvka_mst(4, edges)
    
    # Should return the cheapest edges
    assert len(mst) == 2
    assert set(edge[2] for edge in mst) == {10, 15}

def test_boruvka_mst_empty_graph():
    """Test Boruvka's algorithm with empty edge list."""
    mst = boruvka_mst(3, [])
    assert len(mst) == 0

def test_boruvka_mst_invalid_input():
    """Test Boruvka's algorithm with invalid input."""
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(0, [(0, 1, 10)])
    
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(-1, [(0, 1, 10)])

def test_boruvka_mst_complex_graph():
    """Test Boruvka's algorithm with a more complex graph."""
    edges = [
        (0, 1, 4), (0, 7, 8),
        (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 8, 2), (2, 5, 4),
        (3, 4, 9), (3, 5, 14),
        (4, 5, 10), (4, 6, 2),
        (5, 6, 2), (6, 7, 1), (6, 8, 6),
        (7, 8, 7)
    ]
    
    mst = boruvka_mst(9, edges)
    
    # Expected total weight of MST 
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 37
    
    # MST should have 8 edges (n-1 where n is number of vertices)
    assert len(mst) == 8