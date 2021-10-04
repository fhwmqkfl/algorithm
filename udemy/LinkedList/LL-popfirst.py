class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
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
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        #없어질 노드를 가르키는 temp지정
        temp = self.head
        head = self.head.next
        #노드 다음걸 None으로
        temp.next = None
        self.length -= 1

            #노드가 1개인경우 위의 로직은 tail이 움직이지 못함
        if self.length == 0:  
            self.tail = None
        return temp  


my_linked_list = LinkedList(2)

my_linked_list.append(1)

#return 2 node
print(my_linked_list.pop_first())
#return 1 node
print(my_linked_list.pop_first())
#return None
print(my_linked_list.pop_first())