import sys

sys.stdin = open('input.txt', 'r')

"""스택(LIFO)"""
n, m = map(int, input().split())

num = list(map(int, str(n)))

stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        # 나보다 작은 자료가 stack에 있음 이걸 삭제해버림
        stack.pop()
        m -= 1
    stack.append(x)

# 더 지워야 하는 경우
if m!=0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)