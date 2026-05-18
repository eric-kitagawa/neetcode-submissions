class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}

        for i in range(len(nums)):
            n = nums[i]
            if n in nmap:
                return [nmap[n], i]
            else:
                diff = target - n
                nmap[diff] = i
        
        return [-1, -1]