
n, k = map(int, input().split())

solution = []

##내풀이
for i in range(1,n+1):
    if n % i == 0:
        solution.append(i)

if len(solution) < k:
    print(-1)
else:
  print(solution[k-1])

##강의
cnt = 0
for i in range(1,n+1):
  if n % i == 0:
    cnt += 1
  if cnt == k:
    print(i)
    break
else:
  print(-1)
