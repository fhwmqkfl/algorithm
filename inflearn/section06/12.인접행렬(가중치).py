import sys

sys.stdin = open('input.txt', 'r')

#my solution
n, m = map(int, input().split())
# n*n 그래프를 만들자
a = [[0] * n for _ in range(n)]

for i in range(m):
    L, p, num = map(int, input().split())
    a[L - 1][p - 1] = num

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')

# 인접행렬(무방향)
n, m = map(int, input().split())
# n*n 그래프를 만들자
g = [[0] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()