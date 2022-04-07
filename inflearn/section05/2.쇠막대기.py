import sys

sys.stdin = open('input.txt', 'r')


"""쇠막대기 레이저 절단,레이저는 ()로 표시되며, 쇠막대기는 왼(, 오)로 표현됨 """
s = input()
stack = list()
cnt = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            cnt += len(stack)
        elif s[i-1] == ")":
            cnt += 1

print(cnt)
