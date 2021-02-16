#거스름돈 동전의 최소 개수 구하기

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)
