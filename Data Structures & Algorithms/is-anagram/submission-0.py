class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        set1 = set()
        set2 = set()
        n = len(s)
        m = len(t)

        if n > m or m > n:
            return False

        for i in range(n):
            set1.add(s[i])
            set2.add(t[i])

        if set1 == set2:
            return True

        return False
        