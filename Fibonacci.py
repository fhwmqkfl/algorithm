# 피보나치 수열 1, 1, 2, 3, 5, 8

# my solution
# def DFS(s,r):
#     global cnt
#     if cnt == 7:
#         print(l[-1])
#         return
#     cnt += 1
#     num = s+r
#     l.append(num)
#     print(l)
#     DFS(r,num)
#
# if __name__ == "__main__":
#     l = [1,1]
#     cnt = 1
#     DFS(1,1)

# 1. 함수
def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    for _ in range(1, n):
        a, b = b, a+b
    return a

# print(fib(7))

# 2. 재귀함수
def fib2(n):
    if n==1 or n==2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

# print(fib2(6))


# 3. 제네레이터 방식
# generator 출력할 때, next()로 다음것을 출력⇒ 한단계 늦춤
def fibg():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a


f = fibg()
# print(next(f))
