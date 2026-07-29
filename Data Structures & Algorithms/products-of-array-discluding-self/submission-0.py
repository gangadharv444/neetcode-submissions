class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = 1
        suffix[n-1] = 1
        i = 1
        j = n - 2
        ans = []

        while i <= n and j >= 0:

            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[j] = nums[j+1] * suffix[j+1]
            
            i += 1
            j -= 1

        for i in range(n):
            ans.append(prefix[i]*suffix[i])

        return ans

        



        