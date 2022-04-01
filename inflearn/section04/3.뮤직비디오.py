import sys
sys.stdin = open('input.txt', 'r')
# 기존에 작성한 내용은 반례가 존재

n, m = map(int, input().split())
a = list(map(int, input().split()))
# 추가
maxx = max(a)

lt = 1
rt = sum(a)


def Count(capacity):
    dvd=1
    sum=0
    for x in a:
        # 용량 초과시 새 dvd에 해당 용량값 추가
        if sum+x > capacity:
            dvd+=1
            sum=x
        else:
            sum+=x
    return dvd


while lt <= rt:
    mid = (lt+rt)//2
    # 특정 용량인데 4이면 안되는거지만 2장만에 곡이 저장되면 답이 될 수 있음(3장으로도 가능하니까)
    # 추가 : dvd용량이 적어도 앨범의 음악중 가장 길이긴 maxx보다는 커야됨
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)