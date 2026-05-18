class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        char_map = []

        for n in nums:
            if n in char_map:
                return True
            char_map.append(n)
        
        return False