import sys

sys.stdin = open('input.txt', 'r')

# tsum : sum과 별도로 그 이후 레벨값들을 다 더했을때 weight보다 작으면 계산할 필요 없으니 넘기게함
def DFS(L, sum, tsum):
    global weight
    if sum + (total-tsum) < weight:
        return
    # 합계가 최대무게 넘을 경우 태울 수 없음
    if sum > c:
        return
    # 다 돌았으면 체크
    if L == n:
        if sum > weight:
            weight = sum

    # 안돌았으면
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__ == "__main__":
        c, n = map(int, input().split())
        a = list()
        for i in range(n):
            w = int(input())
            a.append(w)
        weight = 0
        total = sum(a)
        DFS(0, 0, 0)
        print(weight)

