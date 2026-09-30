class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Understand: the function takes an array of numbers and it returns true if there is a duplicate in the array and false otherwise
        #plan: loop through the array and keep track of the number of times a number occurs in the array. and if there is any that is more than one return true if they are all one return false
        nums.sort()
        left = 0 
        right = 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            else:
                left += 1
                right += 1
        return False

        