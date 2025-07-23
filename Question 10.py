# Concept name : Two Pointers

# Question : Move Zeroes
#            Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#            Note that you must do this in-place without making a copy of the array.
          
#                       Example 1:
                      
#                       Input: nums = [0,1,0,3,12]
#                       Output: [1,3,12,0,0]

# Solution : 

class Solution(object):
    def moveZeroes(self, nums):
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        

# Explanation : Use two pointers:
#                             j to scan through the entire list,
#                             i to track the position where the next non-zero element should be placed.
#               Whenever find a non-zero element at nums[j], swap it with nums[i] and increment i.
#               This way, all non-zero elements are moved to the front, and the zeros shift toward the end — all in one pass and in-place.
