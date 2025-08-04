# Concept name : Linked List

  # Question : Odd Even Linked List

  #            Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
  #            The first node is considered odd, and the second node is even, and so on.
  #            Note that the relative order inside both the even and odd groups should remain as it was in the input.
  #            You must solve the problem in O(1) extra space complexity and O(n) time complexity.
              
  #                         Example 1:
                          
                          
  #                         Input: head = [1,2,3,4,5]
  #                         Output: [1,3,5,2,4]

# Solution : 

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=even_head
        return head
        
# Explanation: Group all nodes at odd indices together followed by all nodes at even indices.
#               1. If the list is empty or has only one node, return it as is.
#               2. Use two pointers: 'odd' for odd-positioned nodes, 'even' for even-positioned nodes.
#               3. Save the head of the even list in 'even_head' to attach it later.
#               4. Traverse the list:
#                  - Link current odd node to the next odd node (odd.next = odd.next.next).
#                  - Link current even node to the next even node (even.next = even.next.next).
#                  - Move both pointers forward.
#               5. After traversal, link the last odd node to the head of the even list (odd.next = even_head).
#               6. Return the modified head of the list.
