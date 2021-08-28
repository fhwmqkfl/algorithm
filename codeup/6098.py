m=[[]*10 for _ in range(10)]
for i in range(10):
    m[i]=list(map(int,input().split()))

x=1
y=1
m[x][y]=9

while True:
    if (m[x][y]==2):
        m[x][y]=9
        break
    if (m[x][y+1]!=1):
        m[x][y]=9
        y+=1
    else:
        if(m[x+1][y]!=1):
            m[x][y]=9
            x+=1
        else:
            m[x][y]=9
            break

for i in range(10):
    for j in range(10):
        print(m[i][j],end=' ')
    print()

