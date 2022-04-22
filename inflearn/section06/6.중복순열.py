import sys

sys.stdin = open('input.txt', 'r')
# 입력량이 많고 대량의 자료를 받을때 빠르게 사용
input = sys.stdin.readline

# my solution
# def DFS(l, num, m, cnt):
#     # cnt가 m과 동일하다 : 구슬 다 뽑은거
#     if cnt == m:
#         return
#     else:
#         cnt += 1
#         print(l[num], end=' ')
#         for i in range(len(l)):
#             print("start")
#             DFS(l, num+i, m, cnt)
#     return
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     a = list(range(1,n+1))
#     print(a)
#     cnt = 0
#     DFS(a, 0, m, cnt)

# solution
def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
