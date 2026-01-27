class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for digit in nums:
            if nums.count(digit) > len(nums)//2:
                return digit