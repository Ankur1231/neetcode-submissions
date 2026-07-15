from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict(sorted(Counter(nums).items(),key = lambda item:item[1],reverse=True))
        ans = []
        for item,value in freq.items():
            if len(ans) == k:
                break
            ans.append(item)

        return ans
            




        

        