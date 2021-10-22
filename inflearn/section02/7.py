n = int(input())
# result = []

# for i in range(2, n+1):
#   count = 0
#   for j in range(2,i+1):
#     if i % j == 0:
#       count += 1
    
#   if count == 1:
#     result.append(count)

# print(len(result))

#에라토스테네스 체
ch=[0]*(n+1)
cnt=0

for i in range(2, n+1):
  #소수인지 아닌지 여부
  if ch[i]==0:
    cnt+=1
    for j in range(i, n+1, i):
      ch[j]=1
print(cnt)