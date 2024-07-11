n, m = map(int, input().split())


from itertools import combinations_with_replacement
arr=[]
for j in range(1, n+1):
    arr.append(j)

for tuple in combinations_with_replacement(arr,m):
    print(' '.join(map(str,tuple)))
