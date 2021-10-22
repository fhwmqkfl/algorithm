n, m = map(int, input().split())
empty = []
#빈리스트 0으로 초기화
cnt=[0]*(n+m+3)
max=0
for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j]+=1
  
for i in range(n+m+1):
  if cnt[i]>max:
    max=cnt[i]

for i in range(n+m+1):
  if cnt[i] == max:
    print(i, end=' ')

#result = []

# for i in range(1, n+1):
#   for j in range(1, m+1):
#     if len(empty) == 0 or len(empty) == (i+j-2):
#       empty.insert(i+j-2,1)
#     else:
#       empty[i+j-2] = empty[i+j-2] + 1

# price = max(empty)

# for idx,value in enumerate(empty):
#   if value == price:
#     result.append(idx+2)
  
# print(result)