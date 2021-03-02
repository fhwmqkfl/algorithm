#내 풀이
n = int(input())
num = input().split()

for i in range(n-1, -1, -1):
  print(num[i], end=' ')

#베스트 답안
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

