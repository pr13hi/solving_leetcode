# Concept name : Array / String

# Question : Merge Strings Alternately
            # You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
            # If a string is longer than the other, append the additional letters onto the end of the merged string.
            # Return the merged string.
        
            #             Example 1:
                        
            #             Input: word1 = "abc", word2 = "pqr"
            #             Output: "apbqcr"
            #             Explanation: The merged string will be merged as so:
            #             word1:  a   b   c
            #             word2:    p   q   r
            #             merged: a p b q c r

# Solution : 

class Solution(object):
    def mergeAlternately(self, word1, word2):
        word=""
        length=len(word1) if len(word1)>len(word2) else len(word2)
        for l in range(length):
            if(l<len(word1)):
                word=word+word1[l]
            if(l<len(word2)):
                word=word+word2[l]
        return word

# Explanation : Determine the longer length between the two strings to ensure the loop covers all characters. 
                # Then, using a for loop, iterate through that length and add characters alternately from both word1 and word2, 
                # but only if the current index exists in that string. This way, we can avoid index errors and successfully merge both strings character by character.
