# Concept name : Two Pointers

# Question : Is Subsequence

#            Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#            A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
#            without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
          
#                       Example 1:
                      
#                       Input: s = "abc", t = "ahbgdc"
#                       Output: true

# Solution : 

class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
        
# Explanation : We maintain two pointers:
#                           i for string s
#                           j for string t
#               We iterate through t using j. If characters match (s[i] == t[j]), we move i to check the next character in s.
#               We always move j to keep scanning t.
#               If we successfully match all characters of s by the end of the loop, it means s is a subsequence of t.
