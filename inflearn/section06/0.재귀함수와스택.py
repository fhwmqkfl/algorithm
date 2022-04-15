import sys

sys.stdin = open('input.txt', 'r')


# stack 구조으로 매개변수 x값이 스택에 할당
def DFS(x):
    if x > 0:
        # 1,2,3
        # DFS(x - 1)
        # print(x)

        # 3,2,1
        print(x)
        DFS(x - 1)


if __name__ == "__main__":
    n = int(input())
    DFS(n)