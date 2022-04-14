import sys

sys.stdin = open('input.txt', 'r')

# mysolution : dict에 키 값이 없을시 get함수 이용한다는걸 몰랐음
first = input()
second = input()

l = dict()

for i in first:
    print(i)
    if i in l:
        l[i] += 1
    else:
        l[i] = 1

print("first", l)

for j in second:
    if j in l:
        l[j] -= 1
    else:
        print("NO")
        break

# solution
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        # 값이 다르면 이건 아나그램이 아님
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
