"""
To find the shortest path in a graph represented by the dictionary you provided, you can use a breadth-first search
(BFS) algorithm.
"""
path = {
    "A": ["B", "C"],
    "B": ["D", "E", "C"],
    "C": ["F", "D"],
    "D": ["F", "G"],
    "E": ["G", "F"],
    "F": ["G"],
    "G": []
}

start = "A"
end = "G"


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths


def find_shortest_path(graph, start, end):
    all_paths = find_all_paths(graph, start, end)
    if not all_paths:
        return None
    shortest_path = min(all_paths, key=len)
    return shortest_path


shortest_path = find_shortest_path(path, start, end)
print(shortest_path)
