from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for val,count in freq.items():
            if count > 1:
                return True
        
        return False


        