# mysolution(36188kb/132ms)
n, m = map(int, input().split())
a = list(map(int, input().split()))
stack = list()
for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= m:
                stack.append(a[i] + a[j] + a[k])

print(max(stack))

# better solution(30840kb/72ms)
n, m = map(int, input().split())
# 1. 큰순서대로 나열
a = sorted(list(map(int, input().split())), reverse=True)

stack = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = a[i] + a[j] + a[k]
            if sum <= m:
                stack.add(sum)
                # 2. 여기서 이미 조건을 만족하고 더 작은 숫자는 더해도 의미가 없으니 break(시간단축)
                break
print(max(stack))
