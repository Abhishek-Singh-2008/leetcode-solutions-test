class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        j = len(nums)
        for l in range(j-1):
            if nums[l] in nums[l+1:l+k+1]:
                return True
        return False
                
