import sys

sys.stdin = open('input.txt', 'r')

a = input()
stack = list()
res = ''
#피연산자가 들어오면 바로 스텍에 추가
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            # 스택이 비어있으면 안됨 + 스택의 젤 마지막 자료가 * or /다? 우선순위가 같으므로 밖으로 꺼냄
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            # 소괄호 안의 +- 인경우 ( 이후의 모든 연산자 다 꺼내야함
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            # 여는 괄호를 빼줘야함
            stack.pop()

while stack:
    res += stack.pop()

print(res)