import sys

sys.stdin = open('input.txt', 'r')

# my solution
n = int(input())
a = list(map(int, input().split()))
res = list()
# 역으로 돌면서 숫자 놓기
for i in range(n,0,-1):
    ind = a[i-1]
    res.insert(ind, i)

print(res)

# solution
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n

for i in range(n):
    for j in range(n):
        # 자기자리 찾아 들어가는중
        if a[i] == 0 and seq[j] == 0:
            seq[j] = a[i] + 1
            break
        # 빈자리 확보하는중
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x , end=' ')
