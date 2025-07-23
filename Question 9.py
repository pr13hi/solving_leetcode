# Concept name : Array / String

# Question : String Compression

#            Given an array of characters chars, compress it using the following algorithm:
#            Begin with an empty string s. For each group of consecutive repeating characters in chars:
#            If the group's length is 1, append the character to s.
#            Otherwise, append the character followed by the group's length.
#            The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#            After you are done modifying the input array, return the new length of the array.
          
#            You must write an algorithm that uses only constant extra space.
          
#                         Example 1:
                        
#                         Input: chars = ["a","a","b","b","c","c","c"]
#                         Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#                         Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Solution : 

class Solution(object):
    def compress(self, chars):
        n=len(chars)
        i=0
        idx=0
        while i<n:
            ch=chars[i]
            count=0
            while i<n and chars[i]==ch:
                count+=1
                i+=1
            if count==1:
                chars[idx]=ch
                idx+=1
            else:
                chars[idx]=ch
                idx+=1
                for digit in str(count):
                    chars[idx]=digit
                    idx+=1
        return idx
        

# Explanation : Use two pointers:
#                     i to traverse the original list
#                     idx to overwrite it with the compressed version.
#               For each character ch, count how many times it repeats consecutively.
#                     If it appears only once, just write the character.
#                     If it appears multiple times, write the character followed by the count (as separate digits).
#               Finally, return the new length idx of the compressed array.
              
