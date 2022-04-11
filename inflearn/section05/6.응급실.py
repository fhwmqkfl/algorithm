import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
# 동일한 위험도가 존재할경우 인덱스 순서가 필요함 -> 튜플자료구조
a = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(a)
cnt = 0

while True:
    cur = dq.popleft()
    # 위험도가 제일 높은지 확인
    if any(cur[1] < x[1] for x in dq):
        # 제일 안높으니 뒤로 이동
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
