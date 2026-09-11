class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}
        
        if len(s) != len(t):

            return False

        for ch in s:

            count[ch] = count.get(ch , 0) + 1

        for ch in t:

            count[ch] = count.get(ch , 0) - 1

        for val in count.values():


            if val != 0:

                return False

        return True

     