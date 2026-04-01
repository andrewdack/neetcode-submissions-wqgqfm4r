class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            c = 0
            for j in range(i + 1, len(temperatures)):
                c += 1
                if temperatures[j] > temperatures[i]:
                    break
            else:
                c = 0
            res.append(c)
        return res
                