'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
import sys


sys.stdin = open('dfs_input.txt')
# V 간선 개수, E 노드 개수
V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 0은 판단하지 않고, 간선의 숫자만큼 판단하고 싶어서 +1하는것
# adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    # adjM[v1][v2] = 1
    # adjM[v2][v1] = 1

    adjL[v1].append(v2)
    adjL[v2].append(v1)

for i in adjL:
    print(i)

visit = [1]

visited = [False for _ in range(V + 1)]

path = []

while visit:

    node = visit.pop()
    if visited[node]:
        continue

    visited[node] = True
    path.append(node)

    for i in adjL[node][::-1]:
        if visited[i]:
            continue

        visit.append(i)

print(*path)