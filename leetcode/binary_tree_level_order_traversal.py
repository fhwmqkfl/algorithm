# 이진트리를 bfs(너비 우선 탐색)으로 구현, 주어진 함수가 어떤식으로 노드를 저장하는지 체크하고 접근해야함

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return root

        result = []
        queue = [root]

        while len(queue) > 0:
            level = []

            for i in range(len(queue)):

                node = queue.pop(0)

                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result
