class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDupe = {}

        for n in nums:
            if n in myDupe:
                return True
            myDupe[n] = 1
        
        return False
            