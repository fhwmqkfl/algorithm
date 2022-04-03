import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
meeting = [tuple(map(int, input())) for _ in range(n)]

# a튜플을 종료시간 기준으로 정렬함
meeting.sort(key=lambda x: (x[1], x[0]))

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)

