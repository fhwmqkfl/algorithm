
n = int(input())
a = list(map(int,input().split()))

d =[]

for i in range(24):
    d.append(0)

for j in range(n):
    d[a[j]] += 1

for i in range(1, 24):
  print(d[i], end=' ')

