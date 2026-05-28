class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        table = {} # len 26 tuple -> list of strings

        for word in strs:
            countList = [0 for _ in range(26)]

            for char in word:
                countList[ord(char) - ord('a')] += 1

            countTuple = tuple(countList)
            if countTuple in table:
                table[countTuple].append(word)
            else:
                table[countTuple] = [word]
        
        for s in table:
            result.append(table[s])

        return result