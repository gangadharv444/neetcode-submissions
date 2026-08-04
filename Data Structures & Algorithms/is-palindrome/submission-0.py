class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(char.lower() for char in s if char.isalnum())
        n = len(st)
        i = 0
        j = n - 1

        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        
        return True




        