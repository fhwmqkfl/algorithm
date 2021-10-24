#내풀이
n = int(input())

result = []
for i in range(1,n+1):
  k = list(map(int, input().split()))
  if k[0] == k[1] == k[2]:
    a = 10000 + (k[0] * 1000)
    result.append(a)
  elif k[0] == k[1] or k[0] == k[2] or k[1] == k[2]:
    if k[1] == k[2]:
      a = 1000 + (k[2] * 100)
      result.append(a)
    else:
      a = 1000 + (k[0] * 100)
      result.append(a)
  else:
    num = max(k)
    a = num * 100
    result.append(a)

print(max(result))

#모범답안
n = int(input())
res=0
for i in range(n):
  #이경우 문자로 들어옴
  tmp = input().split()
  #정렬
  tmp.sort()
  a,b,c=map(int, tmp)

  if a == b and b==c:
    money = 10000+a*1000
  elif a==b or a==c:
    money = 1000+a*100
  elif b==c:
    money = 1000+b*100
  else:
    money=c*100
  
  if money>res:
    res=money
print(res)