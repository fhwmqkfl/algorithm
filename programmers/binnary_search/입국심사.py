def solution(n,times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        print("left, right", left, right)
        mid = (left+right)//2
        print("mid", mid)
        total = 0
        for i in times:
            total += (mid // i)
            if total >= n:
                break
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우 : 시간이 충분한것
        if total >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우 : 시간이 모자란것
        elif total < n:
            left = mid + 1

    return answer
