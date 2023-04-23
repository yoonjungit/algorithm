def dfs(graph, n, visited) :
    visited[n] = True
    print(n, end = " ")
    for x in graph[n] :
        if visited[x]==False :
            dfs(graph, x, visited)

graph = [
    [],
    [2, 3],
    [4, 5],
    [6, 7],
    [2],
    [2],
    [3],
    [3]
]

n = 1
visited = {x:False for x in range(1, 8)}
dfs(graph, n, visited)
