# Concept name : Sliding Window

# Question : Longest Subarray of 1's After Deleting One Element

#            Given a binary array nums, you should delete one element from it.
#            Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
            
#                         Example 1:
                        
#                         Input: nums = [1,1,0,1]
#                         Output: 3
#                         Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Solution : 

class Solution(object):
    def longestSubarray(self, nums):
        i=j=0
        n=len(nums)
        count=0
        longest=0
        for j in range(n):
            if nums[j]==0:
                count+=1
            while i<n and count==2:
                if nums[i]==0:
                    count-=1
                i+=1
            longest=max(j-i,longest)
            j+=1
        return longest

# Explanation : Use two pointers i and j for the window.
#               Use count to keep track of how many zeros are in the current window.
#               For every nums[j]: 
#                       If it's a 0, increment count.
#                       If count == 2, shrink the window from the left until the window contains at most one 0.
#               The potential answer is j - i, not j - i + 1, because we are required to delete exactly one element (even if it’s not a 0).
