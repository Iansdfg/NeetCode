class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                old_day, old_temp = stack.pop()
                res[old_day] = day - old_day

            stack.append([day, temp])
        return res
