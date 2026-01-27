class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=[]
        for digit in nums:
            if digit in seen:
                return True
            seen.append(digit)

        return False