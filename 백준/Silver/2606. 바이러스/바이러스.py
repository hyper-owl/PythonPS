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
    
    return len(visited) - 1

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
    return len(visited) - 1

graph = {}
dots = int(input())
lines = int(input())
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

print(DFS(graph, 1))
#print(BFS(graph, 1))