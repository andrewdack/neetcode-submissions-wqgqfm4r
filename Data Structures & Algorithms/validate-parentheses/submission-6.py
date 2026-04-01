class Solution:
    def isValid(self, s: str) -> bool:
        opn = ["{", '(', '[']
        close = ["}", ')', ']']
        stack = []
        for c in s:
            if c in opn:
                stack.append(c)
            elif c in close:
                ind = 0
                if c == close[0]:
                    ind = 0
                elif c == close[1]:
                    ind = 1
                else:
                    ind = 2
                
                if not stack or stack.pop() != opn[ind]:
                    return False
        
        if (not stack):
            return True

        return False
