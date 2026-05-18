class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_map:
                return [diff_map[diff], i]
            diff_map[n] = i
            
        return False
