class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if n in diff_map:
                return [diff_map[n], i]
            diff_map[diff] = i
            
        return False
