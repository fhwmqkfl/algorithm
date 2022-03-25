import sys
sys.stdin = open('input.txt', 'r')

#3/25 격자판 최대합
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# my_solution
result = set()

# 가로
for i in a:
    result.add(sum(i))

# 세로
for i in range(n):
    count = 0
    for j in range(n):
        count += a[j][i]
    result.add(count)

# 대각선
c = 0
d = 0
for i in range(n):
    c += a[i][i]
    d += a[i][n-1-i]

result.add(c)
result.add(d)

print(max(result))


# solution
largest = 0

for i in range(n):
    #초기화
    sum1 = sum2 = 0
    for j in range(n):
        #가로
        sum1 += a[i][j]
        #세로
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

#대각선
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-1-i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
print(largest)