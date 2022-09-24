"""
N개의 동전을 가지고 있음. 이때 동전을 이용해 만들 수 없는 양의 정수 금액중 최솟값을 구하라
N = 5, 동전은 각각 3원,2원,1원,1원,9원 -> 이때 만들 수 없는 금액의 최솟값은 '8'임
"""
# 풀이 : target 변수를 1부터 시작해 더한뒤 만들 수 없는 금액이 되면 그때 리턴하는 방법을 생각
# -> 하지만 늘어나는 수에 맞춰 리스트의 값을 여러개를 유동적으로 계산하게 하는 방법이 떠오르지 않아 풀이에 실패함

# https://github.com/ndb796/python-for-coding-test/issues/28
# 위의 질문 내용을 보고 문제와 답변을 이해할 수 있었음

# solution
n = input()
data = list(map(int, input().split()))
data.sort() # 1,2,5

target = 1
for x in data:
    print("start target", target)
    if target < x:
        break
    target += x
    print("end target", target)

print(target)
