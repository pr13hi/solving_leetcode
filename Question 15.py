# Concept name : Sliding Window

# Question : Maximum Number of Vowels in a Substring of Given Length

#            Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#            Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
                      
#                           Example 1:
                          
#                           Input: s = "abciiidef", k = 3
#                           Output: 3
#                           Explanation: The substring "iii" contains 3 vowel letters.

# Solution : 

class Solution(object):
    def maxVowels(self, s, k):
        vowel='aeiou'
        n=len(s)
        i=0
        j=0
        curr_vowel=0
        max_vowel=0
        while j<n:
            if s[j] in vowel:
                curr_vowel+=1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                max_vowel=max(max_vowel,curr_vowel)
                if s[i] in vowel:
                    curr_vowel-=1
                i+=1
                j+=1
                    
        return max_vowel
            
# Explanation : A window of size k slides over the string.
#               For each character entering the window (s[j]), check if it's a vowel:
#                      If yes, increment the current vowel count.
#               If the current window size is smaller than k, keep expanding.
#               When the window reaches size k:
#                      Update max_vowel if the current count is higher.
#                      Check the character that's leaving the window (s[i]). If it's a vowel, decrement curr_vowel.
#               Slide the window by incrementing both i and j.
