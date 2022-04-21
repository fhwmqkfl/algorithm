import sys

sys.stdin = open('input.txt', 'r')


# 사용, 사용하지않는다 라는 두갈래로 나뉘는 상태트리라는 개념 알아두기
def DFS(v):
    # 종료 지점
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        # 사용하겠다는 의미
        ch[v] = 1
        DFS(v+1)
        # 사용하지 않겠다는 의미
        ch[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)
