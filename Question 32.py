# Concept name : Linked List

 # Question : Maximum Twin Sum of a Linked List

 #            In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
 #            For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
 #            The twin sum is defined as the sum of a node and its twin.
 #            Given the head of a linked list with even length, return the maximum twin sum of the linked list.
            
 #                        Example 1:
                        
 #                        Input: head = [5,4,2,1]
 #                        Output: 6
 #                        Explanation:
 #                        Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
 #                        There are no other nodes with twins in the linked list.
 #                        Thus, the maximum twin sum of the linked list is 6.

# Solution : 

class Solution(object):
    def pairSum(self, head):
        curr=head
        currhalf=head
        newlist=None
        ans=0
        while currhalf and currhalf.next:
            currhalf=currhalf.next.next
            temp=curr.next
            curr.next=newlist
            newlist=curr
            curr=temp
        while curr:
            ans=max(ans,curr.val+newlist.val)
            curr=curr.next
            newlist=newlist.next
        return ans
        
# Explanation: 1. Use fast and slow pointers to reach the midpoint.
#              2. While moving to midpoint, reverse the first half of the list.
#              3. Now, curr points to second half, newlist points to reversed first half.
#              4. Traverse both halves together, calculate pair sums: curr.val + newlist.val.
#              5. Track and return the maximum sum found.
