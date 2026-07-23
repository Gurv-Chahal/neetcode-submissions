# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # O(n + m) Time Complexity
    # O(1) Space
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # this isn't a new list, just a new node
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:

          # if list 1 value is less than list 2
          if list1.val <= list2.val:
            # connect the smaller node after tail (tail.next)
            tail.next = list1
            # advance list1 to the next node
            list1 = list1.next
          # if list 2 value < list 1
          else:
            # connect the smaller node to list 2
            tail.next = list2
            # advance list 2 to next node
            list2 = list2.next

          # advance tail to the next node
          tail = tail.next

        # Connect whichever list still has nodes
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        # Skip the temporary dummy node
        return dummy.next










