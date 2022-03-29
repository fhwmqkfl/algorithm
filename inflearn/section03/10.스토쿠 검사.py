import sys
sys.stdin = open('input.txt', 'r')


def check(x):
    # x축y축 비교
    for i in range(9):
        # 행,열, 그룹체크를 위한 대조군 필요
        dx = [0] * 10
        dy = [0] * 10
        for j in range(9):
            dx[x[i][j]] = 1
            dy[x[j][i]] = 1
        if sum(dx) != 9 or sum(dy) != 9:
            return False
    # 대조군인 블럭을 지정하면
    for i in range(3):
        for j in range(3):
            d = [0] * 10
            # 블럭안의 숫자를 비교
            for k in range(3):
                for s in range(3):
                    d[x[i*3+k][j*3+s]] = 1
            if sum(d) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")