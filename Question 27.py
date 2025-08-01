# Concept name : Queue

# Question : Dota2 Senate

#            In the world of Dota2, there are two parties: the Radiant and the Dire.
#            The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. 
#            The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
#            Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
#            Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
#            Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. 
#            Then if there are n senators, the size of the given string will be n.
#            The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. 
#            All the senators who have lost their rights will be skipped during the procedure.
#            Suppose every senator is smart enough and will play the best strategy for his own party. 
#            Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
          
#                       Example 1:
                      
#                       Input: senate = "RD"
#                       Output: "Radiant"
#                       Explanation: 
#                       The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
#                       And the second senator can't exercise any rights anymore since his right has been banned. 
#                       And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
              
# Solution : 

class Solution(object):
    def predictPartyVictory(self, senate):
        rad=deque()
        dire=deque()
        n=len(senate)
        for i,s in enumerate(senate):
            if s=='R':
                rad.append(i)
            else:
                dire.append(i)
        while rad and dire:
            r=rad.popleft()
            d=dire.popleft()
            if r<d:
                rad.append(r+n)
            else:
                dire.append(d+n)
        return "Radiant" if rad else "Dire"
         
# Explanation : Initialize Queues for Each Party:
#                     Use two deques: rad for Radiant (R) and dire for Dire (D).
#                     Store the indices of each senator.
#               Populate the Queues:
#                     for i, s in enumerate(senate):
#                         if s == 'R':
#                             rad.append(i)
#                         else:
#                             dire.append(i)
#               Simulate Rounds:
#                     While both parties still have senators:
#                           Pop the front senator from both queues.
#                           Whichever index is smaller gets to act first (they ban the other).
#                           The winning senator gets re-added to the queue with an updated index: i + n to simulate the next round.
#                                 if r < d:
#                                     rad.append(r + n)
#                                 else:
#                                     dire.append(d + n)
#               Return the Winner:
#                     When one queue is empty, the other party has all the remaining senators.
#                           return "Radiant" if rad else "Dire"
