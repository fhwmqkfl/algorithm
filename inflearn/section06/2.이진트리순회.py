import sys

sys.stdin = open('input.txt', 'r')

# a = [1, 2, 4, 5, 3, 6, 7]
# 주어진 값만 생각해서 풀이한것임
# 전위순회 : 1 2 4 5 3 6 7
# 중위순회 : 4 2 5 1 6 3 7
# 후위순회 : 4 5 2 6 7 3 1


def DFS(v):
    if v > 7:
        return
    else:
        # 자식노드 호출 전에 print 한다 => 전위순회
        print(v, end=' ')

        # 왼쪽 자식 노드
        DFS(v*2)

        # 자식노드 중간에 print 한다 => 중위순회
        # print(v, end=' ')

        # 오른쪽 자식 노드
        DFS(v*2+1)

        # 자식노드 다 돌고 print 한다 => 후위순회
        # print(v, end=' ')


if __name__ == "__main__":
    DFS(1)
