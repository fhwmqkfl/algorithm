n, m = map(int, input().split())

result = 0

#1번 min()사용
for i in range(n):
  data = list(map(int, input().split()))

  min_data = min(data)

  result = max(result, min_data)

print(result)

#2번 for 두번 사용

# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

