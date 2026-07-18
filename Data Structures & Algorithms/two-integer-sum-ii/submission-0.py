class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_map = {}
        arr = []
        
        for i in range (len(numbers)):
            rem = target - numbers[i]
            if rem in my_map:
                return [my_map[rem] + 1,i + 1]
            my_map[numbers[i]] = i
        
        return []