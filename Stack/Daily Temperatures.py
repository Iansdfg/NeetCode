class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                old_day, old_temp = stack.pop()
                res[old_day] = day - old_day
            stack.append([day, temp])
        return res
        
