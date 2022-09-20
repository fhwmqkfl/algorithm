# 각 자리가 숫자(0-9)로만 이루어진 문자열 S가 주어졌을시,
# 왼쪽->오른쪽 방향으로 숫자를 하나씩 확인하여 +,x연산자를 넣어 결과적으로 만들어 질 수 있는 가장 큰숫자를 구하는 푸로그램을 만들자


# 내 풀이 : 0,1의 경우 곱셈보다 더하는게 나으므로 더하고 나머지는 다 곱하게 처리
# 처음 변수로 지정한 값이 0이라 0번째 인덱스 값은 무조건 더하게 처리(곱하면 계속 0이되므로)
s = input()

result = 0

for i in s:

    num = int(i)

    if result == 0:
        result += num
    else:
        if num <= 1: # 0,1이면 그냥 더함
            result += num
        else: # 그외 숫자는 모두 곱함
            result *= num

print(result)

# solution
# 동일하지만 처음 0인덱스를 if분기가 아닌 result 바로 넣고, range를 1부터 돌게 설정

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num
print(result)