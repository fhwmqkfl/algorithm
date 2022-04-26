import sys

sys.stdin = open('input.txt', 'r')


# solution!!
# 수열 추측하기
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=" ")
        # f를 충족하는 값이 여러번 나올 수 있으므로 그냥 처음 나온값 출력후 바로 시스템 종료
        sys.exit(0)
    else:
        # 순열 만든다
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    # 수열 만들어 나감
    p = [0] * n
    # 초기화[1,1,1,1]
    b = [1] * n
    ch = [0] * (n+1)
    # num = [3C0, 3C1, 3C2 , 3C3]
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i

    DFS(0, 0)
