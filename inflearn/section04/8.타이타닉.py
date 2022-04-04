import sys
from collections import deque

### solution1 ###
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

a.sort()

while a:
    # 리스트(len=1)의 경우 같은값을 두번 더하는게 됨
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > m:
        a.pop()
        cnt += 1
    else:
        a.pop(0)
        a.pop()
        cnt += 1

print(cnt)

### solution2 deque라는 자료구로 구현 ###
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
cnt = 0

while a:
    # 리스트(len=1)의 경우 같은값을 두번 더하는게 됨
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > m:
        a.pop()
        cnt += 1
    else:
        # 여기가 다름!!
        a.popleft()
        a.pop()
        cnt += 1
