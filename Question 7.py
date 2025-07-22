# Concept name : Array / String

# Question : Product of Array Except Self
#            Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#            The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#            You must write an algorithm that runs in O(n) time and without using the division operation.

#                         Example:
                        
#                         Input: nums = [1,2,3,4]
#                         Output: [24,12,8,6]

# Solution : 

class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        ans=[1]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(n):
            ans[i]=prefix[i]*suffix[i]
        return ans

# Explanation : Use two passes to compute the product of all elements except the current one, without using division.
#               First, build a prefix array where each element holds the product of all numbers to its left.
#               Then, build a suffix array where each element holds the product of all numbers to its right.
#               Finally, for each index, multiply the corresponding prefix and suffix values to get the final result.
