class ListNode:
    def __init__(self, val):
        self.val = val    # Store the value/data for this node
        self.next = None  # Pointer to the next node, None means end of list

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)  # Dummy head node, doesn't hold real data
        self.tail = self.head     # Tail starts pointing at the dummy node too

    def insertEnd(self, val):
        self.tail.next = ListNode(val)  # Create new node and link it after current tail
        self.tail = self.tail.next      # Move tail pointer forward to the new last node

    def remove(self, index):
        i = 0
        curr = self.head          # Start traversal from the dummy head
        while i < index and curr: # Walk forward until curr sits just before target index
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr and curr.next:            # Only remove if curr and the target node exist
            if curr.next == self.tail:    # If we're removing the tail node...
                self.tail = curr          # ...update tail to curr since it becomes the new last node
            curr.next = curr.next.next    # Bypass the target node, unlinking it from the list

    def print(self):
        curr = self.head.next             # Skip the dummy head, start at the first real node
        while curr:                       # Traverse until we fall off the end (None)
            print(curr.val, " -> ", end="")  # Print current value followed by an arrow
            curr = curr.next              # Move to the next node
        print()                           # Print a final newline after the full list
