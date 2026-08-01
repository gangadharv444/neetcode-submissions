class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        newnums = list(setnum)
        ans = 0
        n = len(newnums)
        i = 0

        while i < n:
            if newnums[i] - 1 not in setnum:
                count = 1
                curr = newnums[i]
                while curr+1 in setnum:
                    count += 1
                    curr += 1
                ans = max(ans,count)
            i += 1

        
        return ans


        


        
        