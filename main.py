from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # Initialize distances and edge counts
    dist = {v: float('inf') for v in graph}
    edges = {v: float('inf') for v in graph}
    dist[source] = 0
    edges[source] = 0
    
    # Priority queue: (distance, edge_count, vertex)
    pq = [(0, 0, source)]
    
    while pq:
        d, e, u = heappop(pq)
        
        # Skip if we've already found a better path
        if d > dist[u] or (d == dist[u] and e > edges[u]):
            continue
        
     
        for v, weight in graph[u]:
            new_dist = d + weight
            new_edges = e + 1
            
            # Update if we found a shorter path, or same distance with fewer edges
            if new_dist < dist[v] or (new_dist == dist[v] and new_edges < edges[v]):
                dist[v] = new_dist
                edges[v] = new_edges
                heappush(pq, (new_dist, new_edges, v))
    
    # Return result as dict with tuples
    return {v: (dist[v], edges[v]) for v in graph}


def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parents[v] = u
                queue.append(v)
    
    return parents


def get_sample_graph():
    return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    if destination not in parents:
        return ''
    
    path = []
    current = destination
    
    # Trace back from destination to source
    while current in parents:
        path.append(parents[current])
        current = parents[current]
    
    # Reverse to get path from source to destination
    path.reverse()
    
    return ''.join(path)


# Test functions
def test_shortest_shortest_path():
    graph = {
        's': {('a', 1), ('c', 4)},
        'a': {('b', 2)},
        'b': {('c', 1), ('d', 4)}, 
        'c': {('d', 3)},
        'd': {}
    }
    result = shortest_shortest_path(graph, 's')
    print("Test shortest_shortest_path:")
    print(result)
    # Expected: 's' to 'd' can be reached with weight 4 via s->a->b->c->d (4 edges)
    # or s->c->d (2 edges), both have weight 7, but s->c->d has fewer edges
    print()


def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    print("Test bfs_path:")
    print(parents)
    # Expected: {'a': 's', 'b': 's', 'c': 'b', 'd': 'c'}
    print()


def test_get_path():
    parents = {'a': 's', 'b': 's', 'c': 'b', 'd': 'c'}
    print("Test get_path:")
    print("Path to 'd':", get_path(parents, 'd'))  # Expected: 'sbc'
    print("Path to 'a':", get_path(parents, 'a'))  # Expected: 's'
    print("Path to 'b':", get_path(parents, 'b'))  # Expected: 's'
    print()


if __name__ == '__main__':
    test_shortest_shortest_path()
    test_bfs_path()
    test_get_path()
