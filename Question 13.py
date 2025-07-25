# Concept name : Two Pointers

# Question : Max Number of K-Sum Pairs

#            You are given an integer array nums and an integer k.
#            In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.     
#            Return the maximum number of operations you can perform on the array.
          
#                       Example 1:
                      
#                       Input: nums = [1,2,3,4], k = 5
#                       Output: 2
#                       Explanation: Starting with nums = [1,2,3,4]:
#                           - Remove numbers 1 and 4, then nums = [2,3]
#                           - Remove numbers 2 and 3, then nums = []
#                       There are no more pairs that sum up to 5, hence a total of 2 operations.

# Solution : 

class Solution(object):
    def maxOperations(self, nums, k):
        n=len(nums)
        nums.sort()
        i=0
        j=n-1
        ans=0
        while i<j:
            if nums[i]+nums[j]==k:
                i+=1
                j-=1
                ans+=1
            elif nums[i]+nums[j]>k:
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
        return ans

# Explanation : Sort the array to make it easier to find pairs.
#               Use two pointers:
#                     i starts at the beginning  
#                     j starts at the end
#               While i < j:
#                     If nums[i] + nums[j] == k, we found a valid pair → increment ans, move both pointers
#                     If the sum is greater than k, move j left (we need a smaller number)
#                     If the sum is less than k, move i right (we need a bigger number)
