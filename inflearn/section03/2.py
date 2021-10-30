#나오는수28 약수의 개수6

s=input()
res = 0
#문자열에서 숫자만 추출하는 걸 배우고
for x in s:
    if x.isdecimal():
        res = res*10+int(x)

print(res)

#for로 section02.7에서 배웠던 부분 쓰면 될듯 (약수구하기)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt +=1
        
print(cnt)

