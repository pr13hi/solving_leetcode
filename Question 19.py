# Concept name : Prefix Sum

# Question : Find Pivot Index

#           Given an array of integers nums, calculate the pivot index of this array.
#           The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#           If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
#           This also applies to the right edge of the array.
#           Return the leftmost pivot index. If no such index exists, return -1.

#             Example 1:
            
#             Input: nums = [1,7,3,6,5,6]
#             Output: 3
#             Explanation:
#             The pivot index is 3.
#             Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
#             Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Solution : 

class Solution(object):
    def pivotIndex(self, nums):
        left=0
        right=sum(nums)
        for i in range(len(nums)):
            right-=nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1

# Explanation : Calculate the total sum of the array and call it right.
#               Initialize left = 0.
#               Loop through the array:
#                         Subtract the current element nums[i] from right (as it is no longer part of the right sum).
#                         If left == right, return the current index i (this is the pivot).
#                         Add nums[i] to left (moving it to the left sum).
#               If the loop ends without finding a pivot, return -1.
