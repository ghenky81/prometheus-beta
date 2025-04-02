import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from johnsons_algorithm import johnsons_algorithm

def test_basic_graph():
    """Test a simple graph with positive weights."""
    graph = {
        0: [(1, 5), (2, 2)],
        1: [(2, 1), (3, 3)],
        2: [(3, 6)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify the expected shortest paths
    assert result[0][1] == 5  # 0 to 1
    assert result[0][2] == 2  # 0 to 2
    assert result[0][3] == 8  # 0 to 3
    assert result[1][3] == 3  # 1 to 3
    assert result[2][3] == 6  # 2 to 3

def test_graph_with_negative_edges():
    """Test a graph with negative edge weights (but no negative cycles)."""
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify the expected shortest paths
    assert result[0][1] == -1  # 0 to 1
    assert result[0][2] == 2   # 0 to 2
    assert result[0][3] == 1   # 0 to 3

def test_empty_graph():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        johnsons_algorithm({})

def test_single_vertex_graph():
    """Test a graph with a single vertex."""
    graph = {0: []}
    
    result = johnsons_algorithm(graph)
    
    # Verify that the distance to itself is 0
    assert result[0][0] == 0

def test_negative_cycle_detection():
    """Test that a graph with a negative cycle returns None."""
    graph = {
        0: [(1, -1)],
        1: [(2, -1)],
        2: [(0, -1)]
    }
    
    result = johnsons_algorithm(graph)
    
    # Should return None for a graph with a negative cycle
    assert result is None

def test_disconnected_graph():
    """Test a graph with disconnected components."""
    graph = {
        0: [(1, 5)],
        1: [],
        2: [(3, 3)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify that disconnected vertices have infinite distance
    assert result[0][2] == float('inf')
    assert result[2][0] == float('inf')
    assert result[0][0] == 0
    assert result[2][2] == 0

def test_large_graph():
    """Test a larger graph to ensure scalability."""
    graph = {
        0: [(1, 4), (2, 2)],
        1: [(2, 1), (3, 5)],
        2: [(3, 3), (4, 6)],
        3: [(4, 2)],
        4: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Some key distance checks
    assert result[0][4] == 8   # 0 to 4
    assert result[1][4] == 4   # 1 to 4
    assert result[2][4] == 3   # 2 to 4
    assert result[3][4] == 2   # 3 to 4