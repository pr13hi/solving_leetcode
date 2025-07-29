# Concept name : Hash Map / Set

# Question : Equal Row and Column Pairs

#            Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#            A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
          
#                     Example 1:
                    
#                     Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
#                     Output: 1
#                     Explanation: There is 1 equal row and column pair:
#                     - (Row 2, Column 1): [2,7,7]
          
# Solution : 

class Solution(object):
    def equalPairs(self, grid):
        n=len(grid)
        pairs=0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[i][k]!=grid[k][j]:
                        break
                else:
                    pairs+=1
        return pairs

# Explanation : Initialize n as the number of rows/columns in the square grid.
#               Initialize a counter pairs = 0 to track the number of equal row-column pairs.
#               Loop through all possible row and column index combinations (i, j):
#                       For each pair, compare the ith row and jth column element by element.
#                       Use a third loop (k) to iterate from 0 to n-1:
#                               Compare grid[i][k] (element from row) with grid[k][j] (element from column).
#                               If any element doesn’t match, break out of the loop (this row-column pair isn’t equal).
#                       If the loop finishes without breaking, it means all elements matched — so:
#                               Increment pairs by 1.
#               After checking all row-column pairs, return pairs.
