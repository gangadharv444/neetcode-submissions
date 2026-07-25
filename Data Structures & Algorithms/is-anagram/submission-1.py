class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic1 = {}
        dic2 = {}

        n = len(s)
        m = len(t)

        if n > m or m > n:
            return False

        schar = sorted(s)
        sstring = "".join(schar)
        tchar = sorted(t)
        tstring = "".join(tchar)

        for i in range(n):
            if sstring[i] != tstring[i]:
                return False

        return True
        