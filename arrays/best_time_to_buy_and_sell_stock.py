from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit = prices[i] - prices[i - 1]
                max_profit += profit
        return max_profit

    

prices = [7,1,5,3,6,4]
solution = Solution()

print(solution.maxProfit(prices))  # 7

# Time Complexity: O(N)
# Space Complexity: O(1)
