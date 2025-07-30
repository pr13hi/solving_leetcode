# Concept name : Stack

# Question : Removing Stars From a String

#            You are given a string s, which contains stars *.
#            In one operation, you can:
#            Choose a star in s.
#            Remove the closest non-star character to its left, as well as remove the star itself.
#            Return the string after all stars have been removed.
            
#            Note:
#            The input will be generated such that the operation is always possible.
#            It can be shown that the resulting string will always be unique.
             
#                           Example 1:
                          
#                           Input: s = "leet**cod*e"
#                           Output: "lecoe"
#                           Explanation: Performing the removals from left to right:
#                           - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
#                           - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
#                           - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
#                           There are no more stars, so we return "lecoe".
                      
# Solution : 

class Solution(object):
    def removeStars(self, s):
        p=[]
        for i in s:
            if i=="*":
                p.pop()
            else:
                p.append(i)
        return ''.join(p)

# Explanation : Initialize an empty list p to simulate a stack.
#               Traverse each character i in the string s:
#                       If i == '*', remove the last added character by popping from the stack (p.pop()).
#                       Else, add the character to the stack (p.append(i)).
#               After processing the entire string, join the elements in p to form the final result: ''.join(p).
