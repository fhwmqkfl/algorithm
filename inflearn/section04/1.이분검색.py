import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

lt = 0
rt = n-1

while lt <= rt:
    mid = (rt + lt) // 2
    #mid가 찾던 값이다
    if a[mid] == m:
        print(mid+1)
        break
    # 값이 크다? 그럼 오른쪽
    elif a[mid] > m:
        rt = mid-1
    # 값이 작다? 그럼 왼쪽
    else:
        lt = mid+1

