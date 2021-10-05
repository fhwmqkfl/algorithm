N, K = map(int, input().split())
n = list(map(int, input().split()))


#결과값이 중복을 제거 할 수 있게 해야
res=set()

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      res.add(n[i]+n[j]+n[k])

#set을 sorting하기위해 List화
res=list(res)
res.sort(reverse=True)

print(res[K-1])