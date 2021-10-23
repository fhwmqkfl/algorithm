n = int(input())
x = list(input().split())

#뒤집는 함수
def reverse(x):
    l = []
    for i in x:
        i = int(i[::-1])
        l.append(i)
    x = i


#소수인지 확인하는 함수
def isPrime(x):
    for i in x:
        for j in range(2,i+1):
            count = 0
            if i%j==0:
                count += 1
            if count == 2:
                break
            else:
                print(i, end=" ")
