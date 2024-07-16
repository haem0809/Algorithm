import queue
n= int(input())
normal = []
for _ in range(n):
    normal.append(list(input()))

def bfs(arr, si,sj,n,v):
    q = queue.Queue()
    color = arr[si][sj] #현재 컬러

    q.put((si, sj))
    v[si][sj] = 1
    dir = [(-1,0), (1,0), (0,-1),(0,1)]

    while not q.empty():
        ci,cj = q.get()
        for di,dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and arr[ni][nj] == color:
                q.put((ni,nj))
                v[ni][nj] = 1


def count(arr,n):
    v = [[0]*n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if v[i][j]== 0:
                bfs(arr, i,j,n,v)
                cnt += 1

    return cnt

#color grid 만들기
color_grid = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if normal[i][j] == 'R' or normal[i][j] == 'G':
            color_grid[i][j] = 'R'
        else:
            color_grid[i][j] = normal[i][j]

# print(normal)
# print(color_grid)
print(count(normal,n), count(color_grid,n))