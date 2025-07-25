# Concept name : Sliding Window

# Question : Maximum Average Subarray I

#            You are given an integer array nums consisting of n elements, and an integer k.
#            Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
#            Any answer with a calculation error less than 10-5 will be accepted.
          
#                       Example 1:
                      
#                       Input: nums = [1,12,-5,-6,50,3], k = 4
#                       Output: 12.75000
#                       Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Solution : 

class Solution(object):
    def findMaxAverage(self, nums, k):
        s=sum(nums[:k])
        max_sum=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            max_sum=max(max_sum,s)
        return max_sum/float(k)

# Explanation : Initialize the sum of the first k elements.
#               Use a sliding window:
#                   For every index i starting from k, slide the window by one position:
#                         Add the new element entering the window (nums[i])        
#                         Subtract the element leaving the window (nums[i - k])
#                   Keep track of the maximum sum seen so far.
#               Return max_sum / k as the result (convert to float for precision).
