class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = []
        for i in range(0,length):
            prod = 1
            for j in range(0,length):
                if j != i:
                    prod *= nums[j]
            res.append(prod)
        return res