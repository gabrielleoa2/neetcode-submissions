from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #understand:compare the two strings and if they have the same letters with the same amount 
        #plan: split the letters into a list and turn the list into a counter dictionary . if the two dictionary
        #doesn't have a letter in one but it does in the other return false and if the lettrs have different frequencies return false as well
        #otherwise
        #implement
        return Counter(s) == Counter(t)

        