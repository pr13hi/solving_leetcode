# Concept name : Linked List

 # Question : Delete the Middle Node of a Linked List

 #            You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

 #            The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
 #            For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
              
 #                     Example 1:
                      
 #                     Input: head = [1,3,4,7,1,2,6]
 #                     Output: [1,3,4,1,2,6]
 #                     Explanation:
 #                     The above figure represents the given linked list. The indices of the nodes are written below.
 #                     Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
 #                     We return the new list after removing this node.

# Solution : 

class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev:
            prev.next=slow.next
        return head
        
# Explanation: 1. If head is None or has only one node, return None.
#              2. Use two pointers: slow (moves 1 step), fast (moves 2 steps).
#              3. When fast reaches the end, slow is at the middle node.
#              4. Keep track of node before slow using 'prev'.
#              5. Skip the middle node by linking prev.next to slow.next.
#              6. Return the modified head.
