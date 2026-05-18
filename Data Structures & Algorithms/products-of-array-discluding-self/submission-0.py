class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix= []
        p = 1
        for n in nums:
            p *= n
            prefix.append(p)
        
        s = 1
        for n in reversed(nums):
            s *= n
            suffix.append(s)
        suffix.reverse()

        solution = []
        for i in range(len(nums)):
            prefix_num = prefix[i - 1] if i > 0 else 1
            suffix_num = suffix[i + 1] if i < len(suffix) - 1 else 1
            product = prefix_num * suffix_num

            solution.append(product)

        return solution
