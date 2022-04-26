import sys

sys.stdin = open('input.txt', 'r')


# my solution => 중복값 제거 못함
def DFS(L):
    global cnt
    if L == m:
        for i in nums:
            print(i, end=" ")
        cnt += 1
        print()
    else:
        for i in range(L+1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                nums[L] = i
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = [0] * m
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)


# solution
def DFS(L, c):
    global cnt
    if L == m:
        for i in nums:
            print(i, end=" ")
        cnt += 1
        print()
    else:
        for i in range(c, n+1):
            if ch[i] == 0:
                ch[i] = 1
                nums[L] = i
                # c가 아니고 i임!
                DFS(L+1, i+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = [0] * m
    ch = [0] * (n+1)
    cnt = 0
    # 다음 노드에서 for문으로 돌때 기준이 되는 값을 파라미터로 추가
    DFS(0, 1)
    print(cnt)