class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    """
    <create new_node>
    if root == None then root = new_node
    temp = self.root
    while root
        if new_node == temp return False
        if <left else > right
        if None insert new_node else move to next node
    """

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    """
    <contain>
    if root == None return False
    temp = self.root
    while temp is not None
        if < left
        elif > right
        else = return True
    return False
    """
    def contains(self, value):
        # if self.root is None:
        #     return False
        temp = self.root

        while temp is not None:
            if value < value.left:
                temp = temp.left
            elif value < value.right:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


print(my_tree.root.value)            
print(my_tree.root.left.value)        
print(my_tree.root.right.value)        
