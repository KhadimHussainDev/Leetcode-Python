#Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1  # Initialize buy (left) and sell (right) pointers
        profit = 0  # Initialize maximum profit

        while right < len(prices):
            if prices[left] < prices[right]:
                # Calculate current profit if selling on 'right' day
                current_profit = prices[right] - prices[left]
                # Update maximum profit if current profit is greater
                profit = max(profit, current_profit)
            else:
                # Reset buy day to 'right' day if current price is lower
                left = right
            right += 1  # Move to the next day (sell day)

        return profit  # Return the maximum profit