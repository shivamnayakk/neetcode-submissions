class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num , 0) + 1
       
        ## add num in freq
        buckets = [[] for _ in  range(len(nums) + 1)]

        ## add buckets for each numbers

        for num , freq in count.items():
            buckets[freq].append(num)
        # filll the bucket
        
        result = [] ## result me vo num store krenge jo jyada baar aaya hai 

        for i in range(len(buckets) -1 , 0 , -1):

            for num in buckets[i]:

                result.append(num)

                if len(result) == k:
                    return result 




    

        
