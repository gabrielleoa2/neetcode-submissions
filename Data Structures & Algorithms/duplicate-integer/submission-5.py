from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #understand- you're given an array that holds integers that returns true if any integer appears 
        #more than oncein the array else return false
        #plan- loop through the array
        dict = Counter(nums) #creating a dictionary that has a count of all the numbers in the array
        for num in dict: #looping through the numbers/pairs in the dictionary
            if dict[num] > 1: #if the count of the number which is the value in the dictionary is more than one return True
                return True
        return False #if it doesn't return false
            