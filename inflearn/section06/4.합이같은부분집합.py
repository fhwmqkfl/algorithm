import sys

sys.stdin = open('input.txt', 'r')

# my solution(못품)

def DFS(num):
    if num == n:
        # sum값이 나머지 뺀 값이랑 동일하면 yes -> return하는거임
        sec = [x for x in fir if x not in fir]
        if sum(sec) == sum(fir):
            return True
    else:
        fir.append(a[num])
        # 포함되는 경우
        DFS(num+1)
        fir.pop()
        # 포함안되는 경우
        DFS(num+1)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    fir = list()
    if DFS(0):
        print("YES")
    else:
        print("NO")


# solution
def DFS(L, sum):
    # global switch
    # if switch:
    #     return

    # 약간 시간 단축하는 방법
    if sum > total//2:
        return
    # L이 n과 동일할경우 리스트 전부 확인한것임(종료지점)
    if L == n:
        if sum == (total-sum):
            print("YES")
            #프로그램 종료해버림
            # => sys.exit사용 못하는 경우 switch라는 값을 사용해서 하는것
            sys.exit(0)
            # switch = 1
    # 끝나지 않았으면 계속 돈다
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    # switch = 0
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    # 참되는 케이스가 없다? no
    print("NO")
    # if switch==0: print("NO")
