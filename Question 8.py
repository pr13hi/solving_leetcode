# Concept name : Array / String

# Question : Increasing Triplet Subsequence
#            Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
#            If no such indices exists, return false.

#                     Example:
                    
#                     Input: nums = [1,2,3,4,5]
#                     Output: true
#                     Explanation: Any triplet where i < j < k is valid.

# Solution : 

class Solution(object):
    def increasingTriplet(self, nums):
        b=c=float('inf')
        a=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<a:
                a=nums[i]
            elif nums[i]<b and nums[i]>a:
                b=nums[i]
            elif nums[i]<=c and nums[i]>b:
                c=nums[i]
        if c==float('inf'):
            return False
        return True if (a<b) and (b<c) else False
        
# Explanation : Track three values:
#                     a: the smallest number seen so far
#                     b: the next larger number after a
#                     c: the potential third number to form an increasing triplet
#               Iterate through the list:
#                     If found a number smaller than a, update a.
#                     If a number is greater than a but smaller than b, update b.
#                     If a number is greater than b, update c.
#               At the end, if c is still infinity, it means no valid triplet was found.
#               Otherwise, check if a < b < c to confirm the presence of an increasing triplet.
