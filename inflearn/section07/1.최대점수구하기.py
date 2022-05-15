import sys

sys.stdin = open('input.txt', 'r')

def DFS(v,tot,time):
    global  max_num
    if v == n:
        if tot > max_num and time <= m:
            max_num = tot
        return
    if time > m:
        return
    else:
        DFS(v+1, tot+que[v][0], time+que[v][1])
        DFS(v + 1, tot, time)


if __name__ == "__main__":
    # n, 문제 갯수 m 제한시간
    n, m = map(int, input().split())
    que = list()
    for _ in range(n):
        # a,점수 b,시간
        a, b = map(int, input().split())
        que.append((a,b))
    max_num = 0
    DFS(0,0,0)
    print(max_num)