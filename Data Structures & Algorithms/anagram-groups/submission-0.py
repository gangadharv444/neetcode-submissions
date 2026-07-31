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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ans = []
        visited = [False] * n  

        for i in range(n):
            if visited[i]:  
                continue
            
            li = [strs[i]]  
            visited[i] = True
            
            for j in range(i + 1, n):
                if not visited[j] and self.isAnagram(strs[i], strs[j]):
                    li.append(strs[j])
                    visited[j] = True  
            
            ans.append(li)
            
        return ans




        