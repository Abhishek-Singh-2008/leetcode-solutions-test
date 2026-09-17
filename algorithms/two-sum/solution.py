class Solution:    #new test final 2 testing with more time for fall back    def twoSum(self, nums, target):        seen = {}        for i, num in enumerate(nums):            complement = target - num                        if complement in seen:                return [seen[complement], i]            seen[num] = i
class Solution:
    #new test final 2 testing with more time for fall back
    def twoSum(self, nums, target):

        seen = {}

        for i, num in enumerate(nums):

            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i