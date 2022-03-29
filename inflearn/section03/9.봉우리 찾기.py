import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

#가장자리를 0으로 초기화 해주자
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

#각 셀마다 탐색하면서 상하좌우 찾아주기
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)