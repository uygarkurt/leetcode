class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        left_hill = None
        right_hill = None
        hill_found = False
        for i in range(len(arr)-2):
            if arr[i] == arr[i+1] or arr[i+1] == arr[i+2]:
                return False
            if arr[i] < arr[i+1] and arr[i+1] > arr[i+2] and not hill_found:
                left_hill = arr[:i+2]
                right_hill = arr[i+2:]
                hill_found = True
            
        if not left_hill or not right_hill:
            return False
        
        if sorted(left_hill) == left_hill and  sorted(right_hill, reverse=True) == right_hill:
            return True
        return False
