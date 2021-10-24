n = int(input())
for i in range(n):

  s = input()
  s = s.upper()
  #문자열 길이

  size = len(s)
  #답안1
  for j in range(size//2):
    if s[j]!= s[-1-j]:
      print("#%d NO" %(i+1))
      break
  else:
    print("#%d YES" %(i+1))

  #답안2
  # if s == s[::-1]:
  #     print("#%d YES" %(i+1))
  #   else:
  #     print("#%d NO" %(i+1))