n = int(input())
k = list(map(int, input().split()))
avg = round(sum(k)/n)
min=2147000000
#enumerate
for idx, x in enumerate(k):
  #평균값과 학생의 점수차가 적은게 가장 가까운 값이고 그걸 절대값으로 계산
  tmp=abs(x-avg)
  if tmp < min:
    min = tmp
    score = x
    res = idx+1
  
  #동일한 점수를 가진게 여러개일경우
  elif tmp==min:
    if x>score:
      score = x
      res = idx+1

print(avg, res)