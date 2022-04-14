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

# solution 1
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

# solution 2(dict하나로만 실행)
a = input()
b = input()
str1 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str1[x] = str1.get(x, 0) - 1

for x in a:
    if str1.get(x) > 0:
        print("No")
        break
else:
    print("YES")

# solution 3(list) => C++처럼 접근
a = input()
b = input()
# 알파벳이 26 * 2(대.소문자)
str1 = [0] * 52
str2 = [0] * 52
for x in a:
    # 각 알파벳을 아스키 넘버로 바꿔서 처리
    # 대문자는 아스키 넘버 65~90
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1

for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
