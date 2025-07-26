# Concept name : Sliding Window

# Question : Max Consecutive Ones III

#            Given a binary array nums and an integer k, 
#            return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
                       
#                       Example 1:
                      
#                       Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#                       Output: 6
#                       Explanation: [1,1,1,0,0,1,1,1,1,1,1]
#                       Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Solution : 

class Solution(object):
    def longestOnes(self, nums, k):
        i=j=0
        n=len(nums)
        while j<n:
            if nums[j]==0:
                k-=1
            j+=1
            if k<0:
                if nums[i]==0:
                    k+=1
                i+=1
        return j-i

# Explanation : Use two pointers: i (start) and j (end) of the window.
#               Traverse the array with j.
#                     If nums[j] == 0, we're using one flip, so we do k -= 1.
#                     If k < 0, it means we've flipped too many zeros, and need to shrink the window:
#                           Move i forward.
#                           If the element leaving the window (nums[i]) is a 0, we reclaim a flip with k += 1.
#               The window [i, j) always contains at most k flipped zeros.
#               Track the maximum length of such valid windows: j - i.
