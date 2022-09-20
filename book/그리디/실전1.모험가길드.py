# 한 마을에 모험가가 n명 있음. n명의 모험가 대상으로 '공포도'측정(공포도가 높으면 대처능력이 떨어짐)
# 그룹을 안전하게 구성하기 위해 공포도가 X인 모험가는 반스디 X명이상으로 구성한 모험가 그룹에 참여해야함.
# 최대 몇개의 그룹을 만들 수 있는가? 그룹에 포함되지 않는 모험가도 있음

# 첫째줄 N, 둘째줄에는 공포도가 주어지며 공포도의 값은 N이하의 자연수

# 내 풀이 : 가장 작은 수대로 나열후 카운팅하는 방법으로 접근
n = int(input())
ad = list(map(int, input().split()))

ad.sort()

result = 0
l = list()

while len(ad) > 0:

    num = ad.pop(0)
    l.append(num)

    if max(l) == len(l):

        result += 1
        l.clear()
        continue

print(result)


# solution
n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0  # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험자 수

for i in data:
    count += 1
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1
        count = 0

print(result)
