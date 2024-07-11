import queue

def bfs(start_x,start_y,arr,v,n,m):
    q = queue.Queue()
    q.put((start_x,start_y))
    v[start_x][start_y] = 1
    count =0

    dir = [(-1,0), (1,0), (0,-1),(0,1)]

    while not q.empty():
        ci,cj = q.get()

        for di,dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and v[ni][nj] == 0:
                if arr[ni][nj] != "X":
                    q.put([ni,nj])
                    v[ni][nj] = v[ci][cj] +1
                    if arr[ni][nj] == "P":
                        count += 1
    return count

#입력받기
n,m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(input())
    arr.append(row)




#도연이 위치 받기
start_x, start_y = 0,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            start_x, start_y = i, j
            break

#방문 초기화
v =[[0]*m for _ in range(n)]



#BFS수행
count = bfs(start_x,start_y,arr,v,n,m)

#출력
if count == 0:
    print("TT")
else:
    print(count)

