import sys
sys.stdin = open('input.txt', 'r')

"""
곶감 만듬. n*n 격자판으로 회전명령정보가 2(행번호) 0(0왼,1오) 3(회전격자수) 일 경우 2번째 행을 왼쪽으로 3만큼 이동시킴
회전시킨후 모래시계영역에는 몇개의 감이 있는지 합계 계산
"""

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
# 격자판 이동시키기
for i in range(m):
    colum, lr, num = map(int, input().split())
    # 오른쪽 이동이면
    if lr == 1:
        for _ in range(num):
            a[colum-1].insert(0, a[colum-1].pop())
    # 왼쪽이동이면
    else:
        #num만큼 회전
        for _ in range(num):
            #가장 앞의 자리를 꺼냄
            a[colum-1].append(a[colum-1].pop(0))

# 모래시계영역만큼 더하기
s = 0
e = n-1
result = 0
for i in range(n):
    for j in range(s, e+1):
        result += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(result)