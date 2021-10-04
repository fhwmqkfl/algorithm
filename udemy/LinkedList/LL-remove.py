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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
         
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        #temp를 get을 이용해서 가져오는거(과정이 동일하기때문)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        #temp가 None인 경우
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0 or index == self.length:
            return self.prepend(value)

        #temp를 내가 넣을 노드의 인덱스 -1에 위치하게함
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True        

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        #가장 첫번째 노드 삭제시
        if index == 0:
            return self.pop_first()
        #가장 마지막 노드 삭제시
        if index == self.length-1:
            return self.pop()
        #가운데 노드 삭제시
        pre = self.get(index - 1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

my_linked_list = LinkedList(11)
#11 3 23 7
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2), '\n')
my_linked_list.print_list()