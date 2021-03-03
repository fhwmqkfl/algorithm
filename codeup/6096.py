def flip(l, x, y):
    for i in range(19):
        l[x][i] = '1' if l[x][i] == '0' else '0'
        l[i][y] = '1' if l[i][y] == '0' else '0'
l=[]
for i in range(19):
    l.append(input().split())
for i in range(int(input())):
    x,y=map(int, input().split())
    flip(l, x-1, y-1)
for i in range(19):
        print(' '.join(l[i]))
