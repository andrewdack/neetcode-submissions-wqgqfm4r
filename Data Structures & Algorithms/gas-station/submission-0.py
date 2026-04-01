class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasTot = sum(gas)
        costTot = sum(cost)
        if gasTot < costTot:
            return -1

        best = 0
        totalDif = 0
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]

            totalDif += g - c
            if totalDif < 0:
                totalDif = 0
                best = i + 1
            


        return best
