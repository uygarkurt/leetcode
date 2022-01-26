class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k = k-1
        
        def calculator(n, k):
            if n == 1:
                return 0
            elif n==2 and k==0:
                return 0
            elif n==2 and k==1:
                return 1

            new_digit = calculator(n-1, k//2)

            if new_digit == 0:
                new_subset = "01"
            elif new_digit == 1:
                new_subset = "10"
                
            if k%2 == 0:
                return int(new_subset[0])
            elif k%2 == 1:
                return int(new_subset[1])
            
        return(calculator(n, k))
