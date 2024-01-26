class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_day = 0
        sell_day = 1
        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)
            else:
                buy_day = sell_day
            sell_day += 1 
        
        return max_profit

        res = sell_price - buy_price
        if res >0 and sell_day > buy_day:
            return res
        return 0
        
