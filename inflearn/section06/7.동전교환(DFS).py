import sys

sys.stdin = open('input.txt', 'r')

# my solution(fail)
# def DFS(i, s):
#     global tot
#     global count
#     if i > len(coin):
#         return
#     if s + coin[i] > m:
#         return
#     elif s + coin[i] == m and count > i:
#         count = i
#         return
#     else:
#         for j in range(0, n+1):
#             DFS(i+1, s+coin[i])
#
#
# if __name__ == "__main__":
#     n = int(input())
#     coin = list(map(int, input().split()))
#     coin.sort(reverse=True)
#     m = int(input())
#     count = 500
#     tot = 0
#     # i,
#     DFS(0, tot)
#
#     print(count)

# solution

def DFS(L, sum):
    global count
    #time limit 줄이기
    if L > count:
        return
    if sum > m:
        return
    if sum == m:
        if L < count:
            count = L
    else:
        for i in range(n):
            DFS(L+1, sum+L[i])


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)
    m = int(input())
    count = 500
    DFS(0, 0)
    print(count)