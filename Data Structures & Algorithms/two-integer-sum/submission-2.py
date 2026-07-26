class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted((num, idx) for idx, num in enumerate(nums))

        i = 0
        j = len(indexed_nums) - 1

        while i < j:
            summ = indexed_nums[i][0] + indexed_nums[j][0]
            if summ == target:
                return sorted([indexed_nums[i][1], indexed_nums[j][1]])
            elif summ < target:
                i += 1
            else:
                j -= 1

        return [-1, -1]
        