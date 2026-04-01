class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join([c for c in s.lower() if c.isalnum()])
        a = 0
        b = len(s) - 1

        while (a != b and a < b):
            while a < b and not s[a].isalnum():
                a += 1
            while a < b and not s[b].isalnum():
                b -= 1
            if (s[a].lower() != s[b].lower()):
                return False
            a += 1
            b -= 1
        return True
        