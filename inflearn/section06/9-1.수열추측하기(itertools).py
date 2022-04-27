import sys
import itertools as it

sys.stdin = open('input.txt', 'rt')

n, f = map(int, input().split())
b = [1] * n
cnt = 0

for i in range(1, n):
    b[i] = b[i-1]*(n-i)/i

# a = [1,2,3,4]
a = list(range(1, n+1))

# 자동으로 수열로 구해준다!!!!
for tmp in it.permutations(a):
    sum = 0
    for L,x in enumerate(tmp):
        # b 리스트 이용해서 곱해주기!
        sum += (x*b[L])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break

