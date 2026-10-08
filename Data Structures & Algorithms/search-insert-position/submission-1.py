class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        lb = n
        low = 0
        right = n - 1

        while low <= right:

            mid = (low + right) // 2

            if nums[mid] >= target:
                lb = mid
                right = mid - 1

            else:
                low = mid + 1

        return lb