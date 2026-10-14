class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate={}
        for element in nums:
            if element in duplicate:
                return True
            else:
                duplicate[element]=element
        return False
                

        