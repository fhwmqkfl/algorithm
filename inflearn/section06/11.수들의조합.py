import sys

sys.stdin = open('input.txt', 'r')

# my solution
# 조합구하기 응용인듯?
# def DFS(L, c):
#     global cnt
#     # 뽑은 갯수가 k랑 같으면 일단 출력하자
#     if L == k:
#         if sum(num) % m == 0:
#             cnt += 1
#     else:
#         for i in range(c, n):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 num[L] = a[i]
#                 DFS(L+1, i+1)
#                 ch[i] = 0
#
#
# if __name__ == "__main__":
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     m = int(input())
#     cnt = 0
#     ch = [0] * (n+1)
#     num = [0] * k
#     DFS(0,0)
#     print(cnt)

# solution
# DFS매개변수가 3으로
def DFS(L, s, tot):
    global cnt
    # 뽑은 갯수가 k랑 같으면 일단 출력하자
    if L == k:
        if tot%m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, tot+a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
