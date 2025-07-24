class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        res= prices
        for n in range(len(prices)):
            while stack and prices[n]<= prices[stack[-1]]:
                prev = stack.pop()
                res[prev] = res[prev] - prices[n]
            stack.append(n)
        return res
                
