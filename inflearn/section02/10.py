n = int(input())
k = list(map(int, input().split()))

sum=0
cnt=0

for x in k:
  if x==1:
    cnt+=1
    sum+=cnt
  else:
    cnt=0
print(sum)
