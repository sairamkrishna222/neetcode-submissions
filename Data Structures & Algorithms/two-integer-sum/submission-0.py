class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}
        for index,num in enumerate(nums):
            n=target-num
            if n in seen:
                return [seen[n], index]
            else:
                seen[num]=index


        