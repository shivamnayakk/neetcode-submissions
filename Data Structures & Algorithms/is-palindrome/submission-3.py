class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0 # intialzize two pointers

        right = len(s) - 1

        while left < right: # traverse

            while left < right and not s[left].isalnum(): # skip  invalid form left to right

                left += 1
            
            while left < right and not s[right].isalnum(): # skip form tight to left

                right -= 1

            if s[left].lower() != s[right].lower(): # check if left not eqaul to right

                return False 

            left += 1

            right -= 1
        
        return True

            
            

               

                                  


