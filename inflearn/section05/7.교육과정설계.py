import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

# mysolution : 큐를 사용하진 않음..

c = list(input())
n = int(input())
result = ''
empty = list()

for i in range(n):
    st = list(input())

    for j in st:
        if j in c:
            if j in empty:
                continue
            empty.append(j)
    print("empty", empty)
    print(c)
    if c == empty:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")
    empty.clear()

# solution
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    # 각 플랜 검증
    for x in plan:
        # 필수과목임
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    # 잘돌았으나 필수과목을 다 안넣은 케이스가 있음
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))

        else:
            print("#%d NO" % (i + 1))
