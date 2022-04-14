import sys
import heapq as hq

sys.stdin = open('input.txt', 'r')

a = []
while True:
    n = int(input())
    # -1일 경우 종료
    if n == -1:
        break
    # 0일 경우 루트노드값 출력
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            # heappop이라는 함수통해 루트노드값을 pop함
            print(hq.heappop(a))
    else:
        # 최소힙의 형태로 넣어줌
        hq.heappush(a, n)


