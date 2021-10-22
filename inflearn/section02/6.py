#125 15232 97 -> 97


n = map(int, input())
k = list(map(int, input().split()))

"""
입력값(정수) list로 받아서 for반복문을통해 각수의 각 자리수를 더한값을 넣자 (idx, x  enumerate)
"""
#방법1
# def digit_sum(x):
#   sum = 0
#   while x>0:
#     #x를 10으로 나눈나머지가 sum에 누적
#     sum+=x%10
#     #x를 10으로 나눈 몫이 새로운 x
#     x=x//10
#   return sum


#방법2
def digit_sum(x):
  sum=0
  for i in str(x):
    sum+=int(i)
  return sum

max = 0

for x in k:
  tot = digit_sum(x)
  if tot>max:
    max = tot
    res = x

print(res)