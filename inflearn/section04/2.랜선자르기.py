import sys
sys.stdin = open('input.txt', 'r')

# 길이는 1cm ~ 802cm까지임
k, n = map(int, input().split())
line = list()
res = 0
largest = 0
for i in range(k):
    a = int(input())
    line.append(a)

lt = 1
rt = max(line)

def Count(len):
    count = 0
    for x in line:
        count += x // len
    return count

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        # 더 좋은 쪽은 찾기 위해
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
