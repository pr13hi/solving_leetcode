# Concept name : Stack

# Question : Asteroid Collision

#            We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
#            For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
#            Each asteroid moves at the same speed.
#            Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
#            If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
          
           
          
#                         Example 1:
                        
#                         Input: asteroids = [5,10,-5]
#                         Output: [5,10]
#                         Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
          
# Solution : 

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for a in asteroids:
            while stack and stack[-1]>0>a:
                if stack[-1]<abs(a):
                    stack.pop()
                    continue
                elif stack[-1]==abs(a):
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
        
# Explanation : Use a stack to simulate asteroid collisions.
#               Iterate through each asteroid a in the list:
#                     While there’s a possible collision (stack[-1] > 0 and a < 0):
#                           If the incoming asteroid a is stronger (abs(a) > stack[-1]), destroy the top asteroid with stack.pop() and continue checking.
#                           If both are of equal size, destroy both by stack.pop() and break the loop.
#                           If the top of the stack is stronger, break (the current asteroid a is destroyed).
#               If no collision occurred in the while loop, append the asteroid to the stack.
#               After the loop ends, the stack contains the final state of all remaining asteroids.
