class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range (len(nums)):
            rem = target - nums[i] 
            if rem in my_map:
                return [my_map[rem],i]
            my_map[nums[i]] = i

        return False 


        