class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1

        right = max(piles) 

        while left < right : 
            mid = (left + right) // 2

            total_h = 0

            for pile in piles:

                total_h += (pile + mid - 1) // mid

            if total_h > h:

                left = mid + 1
            
            else:

                right = mid

        
        return left


        