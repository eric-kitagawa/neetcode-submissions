class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            candidate_sum = numbers[left] + numbers[right]
            if candidate_sum == target:
                return [left + 1, right + 1]
            elif candidate_sum > target:
                right -= 1
            else:
                left += 1
        
        return -1
            