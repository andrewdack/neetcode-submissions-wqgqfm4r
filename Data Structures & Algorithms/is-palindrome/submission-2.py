class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join([c for c in s.lower() if c.isalnum()])
        print(new)
        a = 0
        b = len(new) - 1

        while (a != b and a < b):
            if (new[a] != new[b]):
                return False
            a += 1
            b -= 1
        return True
        