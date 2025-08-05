# Concept name : Linked List

# Question : Reverse Linked List

#            Given the head of a singly linked list, reverse the list, and return the reversed list.

#                   Example 1:
                  
#                   Input: head = [1,2,3,4,5]
#                   Output: [5,4,3,2,1]

# Solution : 

class Solution(object):
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev_head
        return head
        
# Explanation: 1. Initialize prev = None and curr = head.
#              2. Loop while curr is not None:
#                    a. Store next node in temp = curr.next.
#                    b. Reverse the link: curr.next = prev.
#                    c. Move prev to curr and curr to temp.
#              3. After the loop, prev will be the new head.
#              4. Return prev.
