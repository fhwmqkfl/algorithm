#N,K 입력값 지정해주기
n, k = map(int, input().split())

count = 0

#N이 K이상이라면 K로 계속 나누기
while n >= k:
  while n % k != 0:
    n -= 1
    count += 1
  n //= k
  count += 1

#N이 K보다 작은경우(K로 못나누니까) 1이 되기 전까지 1식 빼기
while n > 1:
  n -= 1
  count += 1

print(count)
