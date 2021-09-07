""" n-queens문제의 해결
기본 가정 : 같은 행에는 퀸을 놓지 않고
구현시 : 같은 열이나, 대각선에 놓이는지를 확인해 본다"""

#column체크하기
#column[i]==column[k]

#diagonal(대각선)체크하기
#절대값이 대각선임
#abs(col[i] - col[k]) == i - k

def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k]) or abs(col[i]-col[k]) == (i-k):
            flag = False
        k += 1
    return flag


def n_queens(i, col):
    n = len(col) - 1
    if (promising(i, col)):
        if i == n:
            print(col[1:n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

n = 4
col = [0] * (n+1)
n_queens(0, col)
