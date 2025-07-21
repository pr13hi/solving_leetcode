# Concept name : Array / String

# Question : Reverse Vowel of a String
#           Given a string s, reverse only all the vowels in the string and return it.
#           The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#                     Example 1:
                    
#                     Input: s = "IceCreAm"
#                     Output: "AceCreIm"
#                     Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Solution : 

class Solution(object):
    def reverseVowels(self, s):
        v=set("aeiouAEIOU")
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            while i<j and s[i] not in v:
                i+=1
            while i<j and s[j] not in v:
                j-=1
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)

# Explanation : Use two pointers — one starting from the beginning (i) and one from the end (j).
#               Store all vowels (both lowercase and uppercase) in a set for quick lookup.
#               Move the i pointer forward until it finds a vowel and the j pointer backward until it finds a vowel.
#               Once both pointers are at vowels, swap them.
#               Repeat this process until the pointers cross, then return the modified string by joining the list back together.

