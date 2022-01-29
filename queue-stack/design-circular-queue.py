class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.queue = [None] * k
        
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        if self.rear == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() == True:
            return False
        if self.front == self.rear:
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max_size
        return True

    def Front(self) -> int:
        null = 0
        for i in self.queue:
            if i == None:
                null += 1
        if null == len(self.queue):
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        null = 0
        for i in self.queue:
            if i == None:
                null += 1
        if null == len(self.queue):
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        null = 0
        for i in self.queue:
            if i == None:
                null += 1
        if null == len(self.queue):
            return True
        return False

    def isFull(self) -> bool:
        null = 0
        for i in self.queue:
            if i == None:
                null += 1
        if null == 0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
