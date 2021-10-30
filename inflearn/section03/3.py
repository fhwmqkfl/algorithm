a= list(range(21))

for i in range(10):
  n, m = map(int, input().split())
  len = (m-n-1)//2
  for j in range(len):
    a[n+j],a[m-j]=a[m-j],a[n+j]
    
a.pop(0)
for x in a:
    print(x, end=" ")
