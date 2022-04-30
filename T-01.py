
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 5일 경우 (1),2,1,(1)

def DFS(L, sum):
    global cnt
    global tot

    if L < 1:
        return
    # 진행할 필요가 없는 값임
    if sum > int(user_input):
        return sum - L

    if sum == int(user_input) - 1 and tot > cnt:
        tot = cnt
        return
    else:
        cnt += 1
        DFS(L + 1, sum + L)
        DFS(L - 1, sum + L)


if __name__ == "__main__":
    user_input = input()
    cnt = 1
    tot = 100001
    DFS(1, 1)
    print(tot + 1)