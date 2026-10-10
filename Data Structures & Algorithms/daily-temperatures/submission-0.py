class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = [] #store val, index

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                val1,ind1 = stack.pop()
                res[ind1] = i-ind1
            stack.append([v,i])
        return res
        