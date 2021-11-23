# 공간 복합도 : O(n)
# 시간 복잡도 : O(n log n)

#helper function이라고도 부름
# [1,3,7,8] [2,4,5,6]

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

#print(merge([1,3,7,8], [2,4,5,6]))

"""
[1,2,3,4,5,6,7,8]

1)Breaks lists in half [1,2]
2)Base case: when len(the_list) is 1
3)Uses merge() to put lists together
"""

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    # 리스트 안의 값이 홀수의 경우 나누면 소수가 발생
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    #이렇게만 할경우 각 리스트가 정렬되지 않음 -> merge적용 어려움
    #return merge(left, right)
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([3,1,4,2]))

