import sys
sys.stdin = open('input.txt', 'r')

count = 0
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 0,1,2번일때 돌아도 됨 왜냐면 5개씩 보니까..!
for i in range(3):
    # j가 행의 역할을함
    for j in range(7):
        #행으로 가는거 확인
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        #열의 경우도 확인한다(회문의 경우 반만 돌면서 확인하면됨)
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)
