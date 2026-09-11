class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 1. Length check
        if len(s) != len(t):
            return False
        
        count = {}

        # 2. Letter gino
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # 3. Letter kato
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        
        # 4. Sab zero hai? (Yahan bracket zaroori hai)
        for val in count.values(): 
            if val != 0:
                return False
                
        return True
     