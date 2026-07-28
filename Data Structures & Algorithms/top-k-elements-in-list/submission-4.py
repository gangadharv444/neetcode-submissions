class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        m = k
        dic = {}
        an = nums

        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        
        an = sorted(an, key=dic.get, reverse=True)

        ans = []

        for i in range(n):
            if m == 0:
                break
            if an[i] not in ans:
                ans.append(an[i])
                m -= 1

        return ans
                

        