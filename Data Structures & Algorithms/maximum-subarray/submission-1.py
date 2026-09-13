class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)

        max_num = nums[0]

        total = 0

        for i in range(0,n):

            total += nums[i]

            max_num = max(max_num , total)
            

            if total < 0:

                total = 0

        return max_num