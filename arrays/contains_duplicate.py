from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


nums_1 = [1,2,3,1]
nums_2 = [1,2,3,4]

solution = Solution()

print(solution.containsDuplicate(nums_1))  # True
print(solution.containsDuplicate(nums_2))  # False

# Time Complexity: O(N)
# Space Complexity: O(N)


