"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""

# 특정 인덱스를 기준으로 왼쪽수의 합과 오른쪽 수의 합이 동일하면, 그 인덱스를 반환하는 문제
# 내 풀이: 인덱스 기준 왼쪽 오른쪽을 계산할수 있게 슬라이싱 이용
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):

            left = sum(nums[:i])
            right = sum(nums[i + 1:])

            if left == right:
                return i

        return -1

# enumerate를 이용해 인덱스와 값을 이용해 합계를 비교하는 방법
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1