class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setlist = set(nums)
        candidates = []
        longest = 0

        for n in nums:
            if n - 1 not in setlist:
                candidates.append(n)
        
        for c in candidates:
            streak = 0
            while c in setlist:
                streak += 1
                c += 1
            longest = max(longest, streak)
        
        return longest
