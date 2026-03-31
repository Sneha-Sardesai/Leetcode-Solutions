class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        if sorted(s) != sorted(t) :
            return False
        return True

""" 
Time Complexity : 
        O(nlogn) -- Best case sorting algorithm -- 
        or 
        O(n^2) -- Worst case sorting algorithm
Space Complexity : 
        O(1) -- for most sorting algorithms -- 
        or 
        O(n) -- if they take up some space while sorting
"""
