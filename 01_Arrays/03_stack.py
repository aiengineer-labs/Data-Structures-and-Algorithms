"""
STACK - TUTORIAL
==================

A stack is a LIFO (Last In, First Out) data structure — the last
element you push in is the first one you pop out. Think of a stack of
plates: you add plates to the top, and you take plates off the top.

Only two ends matter for a stack:
    - the "top" -> where all insertions (push) and removals (pop) happen.

Implementing a stack is trivial using a dynamic array (which we built
from scratch in 01_Arrays/02_Dynamic_Arrays.py) — Python's built-in
`list` is already a dynamic array, so we can just wrap its `append`
and `pop` methods, both of which operate on the *end* of the list.
That end of the list becomes our "top" of the stack.
"""


class Stack:
    def __init__(self):
        """
        Start with an empty stack.

        stack = []   <- no elements yet, nothing to pop.
        """
        self.stack = []

    def push(self, n):
        """
        Push value `n` onto the top of the stack.

        Time complexity: amortized O(1)
            - Python lists are dynamic arrays under the hood, so
              append() behaves just like the pushback() we implemented
              manually in the dynamic array tutorial: usually O(1),
              occasionally O(n) when the list needs to resize, and
              O(1) on average across many pushes.

        Steps:
            1. Add `n` to the end of the underlying list.
            2. That end is our "top" — so `n` is now the top of the stack.

        Example:
            stack = [1, 2]
            push(3) -> stack = [1, 2, 3]   (3 is now on top)
        """
        self.stack.append(n)

    def pop(self):
        """
        Remove and return the value on top of the stack.

        Time complexity: O(1)
            - Removing from the end of a list requires no shifting of
              other elements (unlike removing from the front/middle).

        Steps:
            1. Take the last element off the end of the underlying list.
            2. Return that value to the caller.

        Note: if the stack is empty, list.pop() raises an IndexError
            ("pop from empty list") — this naturally acts as our
            "underflow" check, so we don't need to write one ourselves.

        Example:
            stack = [1, 2, 3]
            pop() -> returns 3, stack = [1, 2]
        """
        return self.stack.pop()


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    s = Stack()

    print("Push 1, 2, 3 onto the stack:")
    for value in (1, 2, 3):
        s.push(value)
    print(s.stack)   # [1, 2, 3]

    print("\nPop twice (LIFO order):")
    print("popped:", s.pop())   # 3 (last one in, first one out)
    print("popped:", s.pop())   # 2
    print("remaining stack:", s.stack)   # [1]
