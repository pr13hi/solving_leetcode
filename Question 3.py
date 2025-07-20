# Concept name : Array / String

# Question : Kids With Greatest Number of Candies
#           There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies,
#           denoting the number of extra candies that you have.
#           Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#           Note that multiple kids can have the greatest number of candies.
          
#                     Example 1:
                    
#                     Input: candies = [2,3,5,1,3], extraCandies = 3
#                     Output: [true,true,true,false,true] 
#                     Explanation: If you give all extraCandies to:
#                     - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
#                     - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
#                     - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
#                     - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
#                     - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Solution :

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        most=max(candies)
        for i in candies:
            if i+extraCandies>=most:
                result.append(True)
            else:
                result.append(False)
        return result

# Explanation : First, find the maximum number of candies that any kid currently has. Then, for each kid, check if giving them the extraCandies would make their total greater than or equal to that maximum.
#               If yes, append True to the result list — meaning that kid can have the greatest number of candies. Otherwise, append False.
#               In the end, return the list of boolean values showing which kids can end up with the most candies.
