"""
1.Binary Tree Preorder Traversal : 전위 순회방식에 대한 내용을 직접 해보는 문제 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Preorder_Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root == None:
            return list()
        else:
            result.append(root.val)
            result += self.preorderTraversal(root.left)
            result += self.preorderTraversal(root.right)
        
        return result
        

""" 
이문제에서 햇갈린 부분은 재귀로 푼다는 방법보다는, 함수의 'root: Optional[TreeNode]'부분이 헷갈렸다.
파이썬 3.5부터 지원된 typing을 잘 사용하지 않아서 일어난 문제인데
변수에 None이 들어올 수도 있으면 Optional을 선언하여 사용하는것이다..!

리스트 형식으로 들어오는 root를 TreeNode클래스의 형식에 맞춰 변형되는 부분을 이해하는데 많은 시간이 걸렸다
"""

"""
2. Binary Tree Inorder Traversal : 중위 순회 방식
전위 순위방식과 동일한 접근이지만 순서가 루트가 아닌 왼쪽노드가 먼저기 때문에 왼쪽-루트-오른쪽 순으로 배치한다
"""
class Inorder_Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root == None:
            return list()
        else:
            result+=self.inorderTraversal(root.left)
            result.append(root.val)
            result+=self.inorderTraversal(root.right)
        
        return result

"""
2. Binary Tree Postorder Traversal : 중위 순회 방식
전위 순위방식과 동일한 접근이지만 순서가 루트가 아닌 왼쪽노드가 먼저기 때문에 왼쪽-루트-오른쪽 순으로 배치한다
"""
class Postorder_Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root == None:
            return list()
        else:
            result += self.postorderTraversal(root.left)
            result += self.postorderTraversal(root.right)
            result.append(root.val)
            
        return result
