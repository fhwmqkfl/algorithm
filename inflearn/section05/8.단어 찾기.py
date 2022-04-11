import sys

sys.stdin = open('input.txt', 'r')
# my solution

n = int(input())
a = list()
for i in range(2*n-1):
    word = input()
    if i <= n-1:
        a.append(word)
    else:
        a.remove(word)

print(a[0])

# solution
n = int(input())
a = dict()

for i in range(n):
    word = input()
    a[word] = 1

for i in range(n-1):
    word = input()
    a[word] = 0

for k, v in a.items():
    if v==1:
        print(k)
        break
