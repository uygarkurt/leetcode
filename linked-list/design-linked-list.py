class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        initial_head = self.head
        counter = 0
        while counter < index:
            self.head = self.head.next
            if self.head == None:
                self.head = initial_head
                return -1
            counter += 1
        ret_val = self.head.val
        self.head = initial_head
        return ret_val

    def addAtHead(self, val: int) -> None:
        if self.head != None:
            new_head = Node(val, self.head)
            self.head = new_head
        else:
            self.head = Node(val)

    def addAtTail(self, val: int) -> None:
        initial_head = self.head
        if self.head != None:
            while self.head.next:
                self.head = self.head.next
            self.head.next = Node(val)
            self.head = initial_head
        else:
            self.head = Node(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return -1
        if self.head == None:
            return -1
        initial_head = self.head
        counter = 1
        while counter < index:
            self.head = self.head.next
            if self.head == None:
                self.head = initial_head
                return -1
            counter += 1
        self.head.next = Node(val, self.head.next)
        self.head = initial_head

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return -1
        initial_head = self.head
        if index == 0:
            self.head = self.head.next
            return -1
        counter = 1
        while counter < index:
            self.head = self.head.next
            if self.head == None:
                self.head = initial_head
                return -1
            counter += 1
        if self.head.next == None:
            self.head = initial_head
            return -1
        self.head.next = self.head.next.next
        self.head = initial_head
        
    def getList(self):
        first_head = self.head
        while self.head:
            print(self.head.val)
            self.head = self.head.next
        self.head = first_head
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
