import sys

sys.stdin = open('input.txt', 'r')

n = int(input())


def binary(x):
    if x == 0:
        return
    else:
        binary(x//2)
        print(x % 2, end='')


binary(n)


