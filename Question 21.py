# Concept name : Hash Map / Set

# Question : Unique Number of Occurrences

#            Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
          
#                   Example 1:
                  
#                   Input: arr = [1,2,2,1,1,3]
#                   Output: true
#                   Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
          
# Solution : 

class Solution(object):
    def uniqueOccurrences(self, arr):
        count={}
        for i in arr:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        freq=list(count.values())
        freqs=set(freq)
        if len(freq)==len(freqs):
            return True
        return False

# Explanation : Count the frequency of each element in the array using a dictionary count.
#               Store all the frequency values in a list freq.
#               Convert the freq list to a set freqs to eliminate duplicates.
#               If the length of freq and freqs is the same, it means all frequencies are unique → return True.
#               Otherwise, return False.
