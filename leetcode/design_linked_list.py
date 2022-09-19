"""
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""

# 기존의 udemy에서 적용한 내용이 기억난 문제, __init__이 고민하는데 가장 오래걸렸는데,
# 리스트로 표현하는게 아닌 node 클래스를 만들는게 어떨까 하는데 시간을 많이 소요했었다
class MyLinkedList(object):

    def __init__(self):
        self.linked = []

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if len(self.linked) - 1 < index:
            return -1
        return self.linked[index]

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.linked.insert(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.linked.append(val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.linked.insert(index, val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if len(self.linked) > index:
            self.linked.pop(index)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)