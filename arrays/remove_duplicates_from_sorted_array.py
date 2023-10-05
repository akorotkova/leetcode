from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:     
                nums[index] = nums[i] 
                index += 1       
        return index


nums =  [0,0,1,1,1,2,2,3,3,4]
solution = Solution()

print(solution.removeDuplicates(nums))  # 5
print(nums)  # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

# Временная сложность O(n)
