class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        sets = set()

        for i in range(len(nums)):

            if nums[i] not in sets:
                sets.add(nums[i])
            else:
                return True

        return False