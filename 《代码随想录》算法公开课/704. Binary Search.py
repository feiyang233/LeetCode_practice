from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:  # [left, right) 如果是等于，就是无效区间

            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1  # mid 已经排除了
            elif nums[mid] > target:
                right = mid  # 因为是右开，mid 不包括在这里
            else:
                return mid

        return -1

