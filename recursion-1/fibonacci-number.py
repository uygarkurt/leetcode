class Solution:
    def __init__(self):
        self.memory = {"name": "uygar"}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.memory:
            return self.memory[n]
        else:
            return self.fib(n-1) + self.fib(n-2)
