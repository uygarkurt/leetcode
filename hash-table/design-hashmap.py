class MyHashMap:

    def __init__(self):
        self.keys = [None] * 1000001
        self.values = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.keys[key] = 1
        self.values[key] = value
            
    def get(self, key: int) -> int:
        if self.keys[key] == None:
            return -1
        
        return self.values[key]
        
    def remove(self, key: int) -> None:
        if self.keys[key] != None:
            self.keys[key] = None
            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
