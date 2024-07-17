n = int(input())
m = int(input())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

plan = []
plan.append(list(map(int, input().split())))
plan = plan[0]

print(arr)
print(plan)


def travel(s,visited,graph):    #s에서 출발
    visited[s] = 1  #현재 도시 방문 표시
    for i in range(n):
        if graph[s][i]==1 and visited[i] == 0:  #연결된 도시 중 방문안한 도시
            travel(i,visited,graph) #방문


visited = [0]*n
travel(plan[0]-1, visited, arr)

result = 'YES'
for city in plan:
    if visited[city-1] == 0:
        result = 'NO'
        break

print(result)

# while city == plan[n - 1]:  # 도착할 때까지
#     for i in range(n):  # road 중에서 탐색
#         if arr[i][0] == city and v[arr[i][1] - 1] != 0:  # 다음 도시와 이어져있고 그게 방문안한도시면
#             city = arr[i][1]  # city 업뎃
#             v[arr[i][1] - 1] = 1  # 방문표시
#             result = 'YES'
#
#         else:
#             result = 'NO'
#             break
