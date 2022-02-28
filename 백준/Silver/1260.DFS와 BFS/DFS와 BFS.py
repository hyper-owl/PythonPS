from collections import deque

def BFS(graph,root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

def DFS(graph, root):
    visited = []
    stack = [root] 

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

graph = {}
dots, lines, root_dot = map(int, input().split())
for i in range(lines):
    start, end = map(int, input().split())
    if start not in graph:
        graph[start] = [end]
    elif end not in graph[start]:
        graph[start].append(end)

    if end not in graph:
        graph[end] = [start]
    elif start not in graph[end]:
        graph[end].append(start)

print(DFS(graph, root_dot))
print(BFS(graph, root_dot))