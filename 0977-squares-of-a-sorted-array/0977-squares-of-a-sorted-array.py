class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums) - 1
        location = len(nums) -1
        result = [0] * len(nums)
        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                result[location] = nums[l] * nums[l]
                l += 1
                location -= 1
            
            elif abs(nums[r]) > abs(nums[l]):
                result[location] = nums[r] * nums[r]
                r -= 1
                location -= 1
    
            else:
                result[location] = nums[l] * nums[l]
                l += 1
                location -= 1

        return result

        