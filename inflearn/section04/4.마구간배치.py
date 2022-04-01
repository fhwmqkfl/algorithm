import sys
sys.stdin = open('input.txt', 'r')

n, c = map(int, input().split())
a = list()
for i in range(n):
    a.append(int(input()))

a.sort()

lt = 1
rt = max(a)
res = 0

def Count(x):
    cnt = 1
    ep = a[0]
    for i in range(1,n):
        if a[i]-ep >= x:
            cnt += 1
            ep = a[i]
    return cnt

while lt <= rt:
    cnt = 1
    mid = (rt+lt)//2
    if Count(mid) < c:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1
print(res)