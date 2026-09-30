class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #understand - 
        #input - an array of nums
        #output - boolean
        # if a number appears twice return true
        #edge case: empty array
        #Plan: 
        # Loop through the nums array, if the number is not in empty dict append into dict with a val of one if the key is there already increment teh value 
        # implement

        dict = {}
        for num in nums: #loop through array:
            if not nums: #edge case
                return False
            if num not in dict: #if the number is not in the dictionaru
                dict[num] = 1
            else: #if the number is in the dictionary
                return True
        return False