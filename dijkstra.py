def dijkstra(graph, start):
    INF = float('inf')

    dist = {node: INF for node in graph}
    dist[start] = 0

    s = {(0, start)}

    while s:
        current_dist, current = min(s)
        s.remove((current_dist, current))

        for neighbour, weight in graph[current]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbour]:

                if dist[neighbour] != INF:
                    s.discard((dist[neighbour], neighbour))

                dist[neighbour] = new_dist
                s.add((new_dist, neighbour))

    return dist


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('B', 1), ('D', 8)],
    'D': []
}

result = dijkstra(graph, 'A')

print(result)