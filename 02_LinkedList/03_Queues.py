class ListNode:
    def __init__(self, val):
        self.val = val    # Store the value/data for this node
        self.next = None  # Pointer to the next node, None means end of list

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None  # left = front of queue, right = back of queue, both start empty

    def enqueue(self, val):
        newNode = ListNode(val)  # Create the new node to add at the back

        # Queue is non-empty
        if self.right:
            self.right.next = newNode  # Link new node after current back node
            self.right = self.right.next  # Move right pointer to the new back node
        # Queue is empty
        else:
            self.left = self.right = newNode  # Single node is both front and back

    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None  # Nothing to remove

        # Remove left node and return value
        val = self.left.val   # Save the value being removed
        self.left = self.left.next  # Move front pointer to the next node
        if not self.left:
            self.right = None  # Queue is now empty, so reset back pointer too
        return val  # Return the removed value

    def print(self):
        cur = self.left            # Start traversal from the front of the queue
        while cur:                 # Traverse until we fall off the end (None)
            print(cur.val, ' -> ', end="")  # Print current value followed by an arrow
            cur = cur.next         # Move to the next node
        print()  # new line
