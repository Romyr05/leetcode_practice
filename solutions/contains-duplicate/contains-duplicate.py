class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        saw = set()

        for i in range(len(nums)):
            saw.add(nums[i])

        if len(saw) != len(nums):
            return True

        return False

        