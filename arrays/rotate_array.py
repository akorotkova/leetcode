from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        lst = [0] * n
        for i in range(n):
            lst[(i + k) % n] = nums[i]
        nums[:] = lst


nums = [1,2,3,4,5,6,7]
k = 3
solution = Solution()

solution.rotate(nums, k)
print(nums)  # [5,6,7,1,2,3,4]

# Time Complexity: O(N)
# Space Complexity: O(N)