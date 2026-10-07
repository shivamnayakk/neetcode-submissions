class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0 
        curr = 0

        mini = float("inf")

        for right  in range(len(nums)):
            curr += nums[right]


            while curr >= target:

                lene = right - left + 1

                mini = min(mini,lene)

                curr -= nums[left]

                left += 1

        if mini == float("inf"):
            return 0

        return int(mini)






        