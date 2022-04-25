import sys

sys.stdin = open('input.txt', 'r')

# my solution(fail..)
# def DFS(L):
#     global cnt
#     if L > m:
#         return
#     if L == m:
#         for i in a:
#             print(i, end=' ')
#         print()
#         cnt += 1
#     else:
#         for i in range(L+1, n+1):
#             a[L] = i
#             DFS(L+1)
#
#
#
# if __name__ == "__main__":
#     n,m = map(int, input().split())
#     a = [0] * m
#     cnt = 0
#     DFS(0)
#     print(cnt)

# solution
def DFS(L):
    global cnt
    if L > m:
        return
    if L == m:
        for i in res:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                # 1을 0으로 되돌려줌
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)
