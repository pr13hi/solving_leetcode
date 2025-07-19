# Concept name : Array / String

# Question : Greatest Common Divisor of Strings

# Solution :

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2!=str2+str1:
            return ""
        if len(str1)==len(str2):
            return str1
        if len(str1)>len(str2):
            return self.gcdOfStrings(str1[len(str2):],str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

# Explanation : First check if str1 + str2 is equal to str2 + str1. If not, return an empty string because that means there's no common pattern that can build both strings. 
# If the condition passes, apply a recursive strategy similar to the Euclidean algorithm used for numbers. If the lengths are equal, return either string as the result.
# If one string is longer, remove the matching prefix (of the shorter string’s length) from the longer string and call the function again.
# This way, gradually reduce the problem until we reach the base case where both strings are equal—which is the greatest common divisor string.

# [Euclidean algorithm -- The Euclidean algorithm is a method to find the greatest common divisor (GCD) of two numbers.
# It works by repeatedly replacing the larger number with the remainder when the larger is divided by the smaller.
# This continues until the remainder becomes zero — and at that point, the other number is the GCD.]
