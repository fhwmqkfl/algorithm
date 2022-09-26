"""
두사람이 서로다른 무개의 볼링공을 고름.
볼링공의 개수 N개, 공의 최대 무게는 자연수 M임(같은 무게여도 다른 공으로 취급, 1 <= M <= 10)
두사람이 고를수 있는 볼링공의 무게의 갯수는?
"""

# 내 풀이 : 중복값을 허용하지 않는 set을 이용하면 된다고 판단해 접근
# 카운트 자체는 원하는 대로 나오지만, 얕은복사로 리스트에 set이 추가되어 실제 리스트 값을 뽑아보면 좋은 방법이 아님을 알 수 있음
n, m = map(int, input().split())
a = list(map(int, input().split()))
result = list()
for i in range(n):
    num = set()
    num.add(a[i])
    for j in range(i+1, n):
        if a[i] == a[j]:
            continue
        num.add(a[j])

        result.append(num)
        num.remove(a[j])

print(len(result))


# solution
"""
각 무게마다 볼링공의 개수를 확인한다.
그리고 무게가 낮은 볼링공부터 무게가 높은 볼링공 까지 순서대로 확인하는 단계를 거친다
공의 최대 무게가 10이라고 했으므로 무게별 공의 갯수를 나타내는 리스트를 만들어 무게별 공의 갯수를 확인하고
이를 계산하는 코드를 만들면 됨
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))

# 1부터 10까지 무게를 나타내는 리스트
weight = [0] * 11

# 무게 카운트
for i in a:
    weight[i] += 1

result = 0
# 1부터 M까지 각 무게에 대한 계산을 한다
for i in range(1, m+1):
    # 먼저 공의 개수 n에서 무게가 i인 볼링공의 개수를 뺀다
    n -= weight[i]
    result += weight[i] * n

print(result)
