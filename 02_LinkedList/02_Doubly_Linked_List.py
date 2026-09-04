class ListNode:
    def __init__(self, val):
        self.val = val    # Store the value/data for this node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)   # Dummy head node, doesn't hold real data
        self.tail = ListNode(-1)   # Dummy tail node, doesn't hold real data
        self.head.next = self.tail # Link dummy head to dummy tail
        self.tail.prev = self.head # Link dummy tail back to dummy head

    def insertFront(self, val):
        newNode = ListNode(val)          # Create the new node to insert
        newNode.prev = self.head         # New node's prev points to dummy head
        newNode.next = self.head.next    # New node's next points to current first node

        self.head.next.prev = newNode    # Old first node's prev now points to new node
        self.head.next = newNode         # Dummy head's next now points to new node

    def insertEnd(self, val):
        newNode = ListNode(val)          # Create the new node to insert
        newNode.next = self.tail         # New node's next points to dummy tail
        newNode.prev = self.tail.prev    # New node's prev points to current last node

        self.tail.prev.next = newNode    # Old last node's next now points to new node
        self.tail.prev = newNode         # Dummy tail's prev now points to new node

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head  # Second node's prev now points to dummy head
        self.head.next = self.head.next.next  # Dummy head's next now skips the removed node

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail  # Second-to-last node's next now points to dummy tail
        self.tail.prev = self.tail.prev.prev  # Dummy tail's prev now skips the removed node

    def print(self):
        curr = self.head.next        # Skip the dummy head, start at the first real node
        while curr != self.tail:     # Traverse until we reach the dummy tail
            print(curr.val, " -> ")  # Print current value
            curr = curr.next         # Move to the next node
        print()                      # Print a final newline after the full list
