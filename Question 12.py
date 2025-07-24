# Concept name : Two Pointers

# Question : Container With Most Water

#            You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#            Find two lines that together with the x-axis form a container, such that the container contains the most water.
#            Return the maximum amount of water a container can store.
#            Notice that you may not slant the container.
                
#                       Example 1:
                      
#                       Input: height = [1,8,6,2,5,4,8,3,7]
#                       Output: 49
#                       Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
#                       In this case, the max area of water (blue section) the container can contain is 49.

# Solution : 

class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        volume=0
        if n==2:
            return min(height[left], height[right])
        while left<right:
            dist=right-left
            curr_vol=dist*min(height[left],height[right])
            volume=max(curr_vol,volume)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return volume

# Explanation :We use two pointers:
#                         left starting from index 0
#                         right starting from the end of the array
#              At each step:              
#                         Calculate the area = width × min(height[left], height[right])              
#                         Update volume if the new area is larger              
#                         Move the pointer pointing to the shorter line inward — hoping for a taller line and possibly more water              
#              We keep doing this until left meets right.
