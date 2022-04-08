import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
stack = list(range(1,n+1))

dq = deque(stack)

while dq:
    for _ in range(1, m-1):
        #외치는 사람을 맨 뒤로 보냄
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()


