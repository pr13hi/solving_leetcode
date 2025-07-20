# Concept name : Array / String

# Question : Can Place Flowers
#           You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#           Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
#           return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
          
#                     Example 1:
                    
#                     Input: flowerbed = [1,0,0,0,1], n = 1
#                     Output: true

# Solution : 

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n-=1
                if n==0:
                    return True
                flowerbed[i]=1
        return False

# Explanation : Loop through each spot in the flowerbed and check if a flower can be planted there.
#               A flower can only be placed if the current spot is empty (0), and both its neighbors (if they exist) are also empty or out of bounds (start/end of the list).
#               If it's safe, place a flower there (mark it as 1) and decrease n by 1.
#               If n becomes zero at any point, return True early.
#               If the loop finishes and there are still flowers left to place, return False.
