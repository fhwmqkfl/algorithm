import sys

sys.stdin = open('input.txt', 'r')

# 후위식 연산
n = input()
stack = list()
result = 0
for i in n:
    num = 0
    if i.isdecimal():
        stack.append(int(i))
    elif i == '+':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1+n2)
    elif i == '-':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2-n1)
    elif i == '*':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2*n1)
    elif i == '/':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2/n1)

print(stack[0])