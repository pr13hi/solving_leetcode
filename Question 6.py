# Concept name : Array / String

# Question : Reverse Words in a String
#            Given an input string s, reverse the order of the words.
#            A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#            Return a string of the words in reverse order concatenated by a single space.
#            Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

#                     Example 1:
                    
#                     Input: s = "the sky is blue"
#                     Output: "blue is sky the"

# Solution : 

class Solution(object):
    def reverseWords(self, s):
        word=s.split()
        rev_word=word[::-1]
        return " ".join(rev_word)
        

# Explanation : First use .split() to break the input string s into a list of words, automatically removing any extra spaces.
#               Then, reverse the list using slicing ([::-1]).
#               Finally, use " ".join() to join the reversed words back into a single string with exactly one space between them.
#               This gives the input string with its words in reverse order and clean spacing.
