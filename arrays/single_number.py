from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


solution = Solution()

nums_1 = [2, 2, 1, 3, 3]
nums_2 = [1]

print(solution.singleNumber(nums_1))  # 1
print(solution.singleNumber(nums_2))  # 1

# Time Complexity: O(N)
# Space Complexity: O(N)
