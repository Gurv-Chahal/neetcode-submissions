class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        
        # check whether the index exists
        if index < 0 or index >= self.size:
            return -1

        # begin at index 0
        curr = self.head

        # iterate over index times
        for i in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        
        # create new node
        newNode = ListNode(val)

        # New node points to the old head node
        newNode.next = self.head

        # head now points to the new node
        self.head = newNode

        # increase size by 1
        self.size += 1

    def addAtTail(self, val: int) -> None:
        
        # create a new node
        newNode = ListNode(val)

        # if list is empty
        if self.head is None:
            self.head = newNode
        else:
            # find the current final node
            # iterate to the end
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            
            # once the loop exits then we are at final node
            curr.next = newNode

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        # index is greater than size
        if index > self.size:
            return

        # inserting at index 0 is same as adding at head
        if index == 0:
            self.addAtHead(val)
            return
        
        newNode = ListNode(val)

        # find node immediately before insertion index
        curr = self.head
        for i in range(index - 1):
            curr = curr.next
        
        # insert without losing the remaining list
        newNode.next = curr.next
        curr.next = newNode

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        
        # first check if index is valid
        if index < 0 or index >= self.size:
            return

        # if index is at head
        if index == 0:
            self.head = self.head.next
        else:
            # find the node before the one being deleted
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            
            # skip the node at that index
            curr.next = curr.next.next
        
        self.size -= 1
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)