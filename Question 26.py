# Concept name : Stack

# Question : Decode String

#            Given an encoded string, return its decoded string.
#            The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
#            Note that k is guaranteed to be a positive integer.
#            You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
#            Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#            The test cases are generated so that the length of the output will never exceed 105.
          
#                   Example 1:
                  
#                   Input: s = "3[a]2[bc]"
#                   Output: "aaabcbc"
                      
# Solution : 

class Solution(object):
    def decodeString(self, s):
        stack=[]
        curr_str=""
        curr_num=0
        for c in s:
            if c.isdigit():
                curr_num=curr_num*10+int(c)
            elif c=="[":
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num=0
                curr_str=""
            elif c=="]":
                prev_str=stack.pop()
                prev_num=stack.pop()
                curr_str=prev_str+curr_str*prev_num
            else:
                curr_str+=c
        while stack:
            curr_str=stack.pop()+curr_str
        return curr_str

# Explanation : Initialize an empty stack, an empty string curr_str, and an integer curr_num = 0.
#               Iterate through each character c in the input string s:
#                     If c is a digit:
#                           Build the multiplier curr_num (to handle numbers > 9), i.e., curr_num = curr_num * 10 + int(c).
#                     If c is [:
#                           Push curr_num and curr_str onto the stack.
#                           Reset curr_str to "" and curr_num to 0 for the new substring.
#                     If c is ]:
#                           Pop prev_str and prev_num from the stack.
#                           Update curr_str = prev_str + curr_str * prev_num, i.e., repeat the current string and append to the previous one.
#                     If c is a character:
#                           Add it to curr_str.
#               After the loop:
#                     If any string pieces remain in the stack, pop and concatenate them with curr_str.
#               Return the fully decoded string.
