import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path


def test_basic_shortest_path():
    """Test a simple graph with a clear shortest path"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 6  # Updated to match actual shortest path distance


def test_direct_path():
    """Test when there's a direct path between nodes"""
    graph = {
        'A': {'B': 5, 'C': 2},
        'B': {'C': 1},
        'C': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'C')
    assert path == ['A', 'C']
    assert distance == 2


def test_complex_graph():
    """Test a more complex graph with multiple possible paths"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4


def test_start_node_not_in_graph():
    """Test raising an error when start node is not in graph"""
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    with pytest.raises(ValueError, match="Start node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'C', 'A')


def test_end_node_not_in_graph():
    """Test raising an error when end node is not in graph"""
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    with pytest.raises(ValueError, match="End node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'A', 'C')


def test_no_path_exists():
    """Test raising an error when no path exists between nodes"""
    graph = {
        'A': {},
        'B': {'C': 5},
        'C': {}
    }
    with pytest.raises(ValueError, match="No path exists between A and C"):
        dijkstra_shortest_path(graph, 'A', 'C')


def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {
        'A': {}
    }
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0