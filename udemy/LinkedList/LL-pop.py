class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        #리스트에 아무노드도 없는경우
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        #그외
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None #그 다음에 노드를 pop하는거
        self.length -= 1
        
        #노드가 하나의 경우 위의 로직에서 length는 0이지만 head,tail이 원래 노드를 가르키게됨)
        if self.length == 0:
            self.head = None
            self.tail = None
        #우리가 제거한 노드인 temp를 리턴
        return temp.value



my_linked_list = LinkedList(1)

my_linked_list.append(2)

#(2)items
print(my_linked_list.pop())
#(1)items
print(my_linked_list.pop())
#(0)items
print(my_linked_list.pop())
