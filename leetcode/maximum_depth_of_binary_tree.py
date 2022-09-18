"""
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 나의 풀이 : 실패
# 원인 : DFS를 생각하고 재귀를 이용해 풀려고 생각. 하지만 뎁스를 카운트 하는 방법을 잘못 생각
# 아래방법대로 하게되면 result, depth가 계속 0인상태로 시작됨
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        result = 0
        depth = 0

        depth += 1
        if result < depth:
            result = depth
        if root.left is not None:
            self.maxDepth(root.left)
        if root.right is not None:
            self.maxDepth(root.right)

        return result

# Solution 1 : DFS로 접근해 재귀 함수로 이용한 방식.
class Solution(object):
    def maxDepth(self, root):

        if root is None:
            return 0
        else:
            lefth = self.maxDepth(root.left)
            righth = self.maxDepth(root.right)

        return 1 + max(lefth, righth)


# Solution 2 : BFS를 활용하여 푼 예시
# binary_tree_level_order_traversal에서 동일하게 풀었다
# 해당 방법이 익숙치 않아 좀더 학습해야 함

from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        depth = 0

        Q = deque([root])
        while Q:
            depth += 1
            for _ in range(len(Q)):
                cur_node = Q.popleft()
                if cur_node.left:
                    Q.append(cur_node.left)
                if cur_node.right:
                    Q.append(cur_node.right)

        return depth
