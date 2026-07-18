class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        flag,output = 0,0
        nums.sort()
        for i in range(len(nums)):
            flag+=1
            output = max(flag,output)
            if i == len(nums) - 1:
                break
            if nums[i] == nums[i+1]:
                flag-= 1
                continue
            if nums[i] + 1 != nums[i+1]  :
                flag = 0
        
        return output
        