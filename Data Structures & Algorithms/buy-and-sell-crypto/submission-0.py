class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,maxP = 0,1,0

        while(r < len(prices)):
            
            if prices[l] >= prices[r]:
                l = r
                r+=1
            else:
                sum = prices[r] - prices[l]
                maxP = max(maxP, sum)
                r+=1
        
        return maxP
        