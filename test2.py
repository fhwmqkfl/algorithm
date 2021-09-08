import sys

#시간, 탑승정원, 그리고 입력된 순서
def elevator(t, m, case):
  count = 0
  result = []
  for i in range(1,t+1):
    if count == m:
      return i
      break
    #태우는 과정
    else:
      for j in range(1,i+1):

        newcase = case[0:i]

        #층수랑 value값이 동일하다? => 내림
        if newcase[j-1][0] < i and newcase[j-1][1] == i:
          count -= 1

        #층수랑 대기층 값이 동일하다? => 탑승
        if newcase[j-1][0] == i:
          count += 1

      result.append(count)
  return max(result)-m


#케이스 c
c = int(sys.stdin.readline().rstrip())

for i in range(1,c+1):
  #n(층수),m(인원),t(탑승횟수))
  n, m, t = map(int, sys.stdin.readline().split())
  case = []
  for i in range(t):
    case.append(list(map(int, sys.stdin.readline().split())))
  print(elevator(t, m, case))

