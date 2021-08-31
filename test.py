""" arr = [-1, 0, 3, 4, 19]
n = 3
result = 2"""

# 순차탐색의 경우
# 못찾을시 -1
def test(arr, n):
    #arr의 리스트 길이를 for문으로
    lenth = len(arr)
    result = -1
    for i in range(lenth):
        if arr[i] == n:
            result = i
    return result

#print(test([-1,0,3,4,19], 3))



#이진 탐색을 통해서 처리
def binary_search(arr, target):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        #타겟보다 값이 작으면 왼쪽
        elif arr[mid] > target:
            end = mid -1
        #타겟보다 값이 많으면 오른쪽i
        else:
            end = mid + 1

    return mid

print(binary_search([-1,0,3,4,19], 3))
