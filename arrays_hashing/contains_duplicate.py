#Contains Duplicate
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
from typing import List



class Solution:
    def has_duplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            if num in seen:
                print(f"num: {num}, seen: {seen}")
                return True
            else:
                seen.append(num)
                print(f"num: {num}, seen: {seen}")
        return False

if __name__ == '__main__':
    nums = [1, 2, 3, 3]
    result = Solution().has_duplicate(nums)
    print(result)