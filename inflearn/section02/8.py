n = int(input())
a=list(map(int, input().split()))

def reverse(x):
  res = 0
  while  x>0:
    #x의 1의자리
    t=x%10
    res=res*10+t
    #몫
    x=x//10
  return res

def isPrime(x):
  #100, 1000이 리버스되면 1임
  if x ==1:
    return False
  #약수는 숫자의 절반만 존재!
  for i in range(2, x//2+1):
    if x%i==0:
      return False
  else:
    return True

for x in a:
  tmp=reverse(x)
  if isPrime(tmp):
    print(tmp, end = " ")

# x = list(input().split())

# #뒤집는 함수
# def reverse(x):
#     l = []
#     for i in x:
#         i = int(i[::-1])
#         l.append(i)
#     x = i


# #소수인지 확인하는 함수
# def isPrime(x):
#   reverse(x)
#   for i in x:
#       for j in range(2,i+1):
#           count = 0
#           if i%j==0:
#               count += 1
#           if count == 2:
#               break
#           else:
#               print(i, end=" ")
