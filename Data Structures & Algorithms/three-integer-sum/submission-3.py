class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1
            while l < r:
                left = nums[l]
                right = nums[r]

                candidate = left + right

                if candidate == target:
                    solution.append([target * -1, left, right])
                    while l < len(nums) - 1 and nums[l + 1] == left:
                        l += 1
                    while r > 0 and nums[r - 1] == right:
                        r -= 1
                    l += 1 
                    r -= 1
                    
                elif candidate > target:
                    r -= 1
                else:
                    l += 1
    
        return solution


