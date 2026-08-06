# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # recursive solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case: empty list or one remaining node
        if head is None or head.next is None:
          return head

        # call recursion on head.next and save it
        newHead = self.reverseList(head.next)
        
        # make the next node point backward to the current node
        head.next.next = head

        # remove the current nodes old forward connection
        head.next = None

        # return the new beginning of the reversed list
        return newHead