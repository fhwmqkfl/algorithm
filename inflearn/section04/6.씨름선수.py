import sys

sys.stdin = open('input.txt', 'r')


# 씨름선수(그리디)
n = int(input())
entry= [tuple(map(int, input().split())) for _ in range(5)]

cnt = 0
for i in range(n):
    win = 0
    for j in range(n):
        # 키 or 몸무게 둘중하나라도 떨어지면 탈락임 아니면 그냥 계속 고고
        if entry[i][0] > entry[j][0] or entry[i][1] > entry[j][1]:
            win += 1
        else:
            continue
        if win == (n-1):
            cnt += 1

print(cnt)

# solution
n = int(input())
entry= [tuple(map(int, input().split())) for _ in range(5)]

entry.sort(reverse=True)
largest = 0
cnt = 0

for x, y in entry:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)