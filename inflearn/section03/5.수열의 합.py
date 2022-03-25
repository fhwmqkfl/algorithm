import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())
a = list(map(int, input().split()))

# my_solution
count = 0
for i in range(n):
    if a[i] == m:
        count += 1
    for j in range(i+1, n):
        b = a[i:j]
        if sum(b) == m:
            count += 1

print(count)
# answer

lt = 0
#rt가 기준점으로 움직임
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt+=1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        # 오른쪽으로 이동시킴
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)


