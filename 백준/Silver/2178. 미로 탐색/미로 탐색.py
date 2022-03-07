from collections import deque

n, m = map(int,input().split())

graph = []

for row in range (n):
    graph.append(list(map(int,input())))

def bfs(x, y):
    move = [(-1,0),(1,0),(0,-1),(0,1)] #(상,하,좌,우)
    
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for dx, dy in move:
            now_x = x + dx
            now_y = y + dy

            if now_x < 0 or now_x >= n: # x가 제한범위 밖이거나
                continue
            if now_y < 0 or now_y >= m: # y가 제한범위 밖이거나
                continue
            if graph[now_x][now_y] == 0: # 바뀐 점이 벽이라면 넘긴다.
                continue
            
            if graph[now_x][now_y] == 1:
                graph[now_x][now_y] = graph[x][y] + 1 # 이전의 값에 +1 한 값을 옮긴 칸에 표시 (몇 번 이동했는지를 나타냄)
                queue.append((now_x, now_y))
    
    return graph[n-1][m-1] # 도착지에 적힌 값을 리턴

print(bfs(0,0))