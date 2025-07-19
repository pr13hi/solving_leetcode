# Concept name : Array / String

# Question : Merge Strings Alternately

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
