class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Understand
        #input: two strings
        #output:Boolean
        #Edge case: empty strings
        #Plan
        #sort the strings use the two ptr method with a ptr at the beginning and end of each string and 
        if len(s) != len(t):
            return False
        sorted_s  = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        print(sorted_s)
        print(sorted_t)
        s_ptr = 0
        t_ptr = 0
        while s_ptr < len(sorted_s) and t_ptr < len(sorted_t):
            if sorted_s[s_ptr] == sorted_t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                return False
        return True