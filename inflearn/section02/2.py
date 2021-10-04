T = int(input())

result = 0

for i in range(T):
  N, s, e, k = map(int, input().split())
  n = list(map(int, input().split()))
  n = n[s-1:e]
  n.sort()
  result = n[k-1]
  print("#{}".format(i+1), result)
  #print("#%d %d" %(i+1, result))
  