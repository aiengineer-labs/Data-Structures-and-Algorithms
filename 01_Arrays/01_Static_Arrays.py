"""
STATIC ARRAY - TUTORIAL
========================

A static array is a fixed-size block of memory. Once created, its
CAPACITY (total slots available) never changes.

We track two separate numbers:
    - capacity -> total number of slots the array has (fixed).
    - length   -> number of slots currently holding "real" data.

Since Python lists are dynamic by nature, we simulate a static array by
pre-filling a list with placeholder values (0) up to a fixed capacity,
and only treating the first `length` elements as meaningful data.

Example:
    arr      = [5, 3, 8, 0, 0]   (capacity = 5)
    length   = 3                 (only 5, 3, 8 are "real")
    unused   = arr[3], arr[4]    (reserved but empty slots)
"""


def insertEnd(arr, n, length, capacity):
    """
    Insert value `n` at the end of the array (position `length`).

    Time complexity: O(1)
        - We're inserting directly at a known index, no shifting needed.

    Steps:
        1. Check there's room left (length < capacity).
        2. Place `n` at index `length` (the next open slot).
        3. (Caller is responsible for incrementing length afterward.)
    """
    if length < capacity:
        arr[length] = n


def removeEnd(arr, length):
    """
    Remove the last element of the array (position `length - 1`).

    Time complexity: O(1)
        - We're removing directly from a known index, no shifting needed.

    Steps:
        1. Check the array isn't already empty (length > 0).
        2. Overwrite the last "real" value with a default (0).
        3. (Caller is responsible for decrementing length afterward.)
    """
    if length > 0:
        # Overwrite last element with a default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0


def insertMiddle(arr, i, n, length):
    """
    Insert value `n` at index `i`, shifting existing elements right
    to make room.

    Time complexity: O(n)
        - In the worst case (i = 0), every element must shift right.

    Assumptions:
        - `i` is a valid index.
        - The array is not already full (there's a free slot to shift into).

    Steps:
        1. Walk backward from the last element down to index `i`.
        2. Shift each element one position to the right.
        3. Once the gap is opened at index `i`, place `n` there.

    Example (inserting 9 at index 1):
        Before: [1, 2, 3, 0]   length = 3
        Shift:  [1, 2, 3, 3]   -> arr[3] = arr[2]
        Shift:  [1, 2, 2, 3]   -> arr[2] = arr[1]
        Insert: [1, 9, 2, 3]   -> arr[1] = 9
    """
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    # Insert at i.
    arr[i] = n


def removeMiddle(arr, i, length):
    """
    Remove the value at index `i`, shifting subsequent elements left
    to close the gap.

    Time complexity: O(n)
        - In the worst case (i = 0), every remaining element must shift left.

    Assumptions:
        - `i` is a valid index.

    Steps:
        1. Walk forward from index `i + 1` to the end of the array.
        2. Shift each element one position to the left, overwriting
           the value before it.
        3. No need to explicitly "clear" the old last value — the next
           insertEnd/removeEnd call will treat it as unused since it's
           now past the (soon-to-be-decremented) length.

    Example (removing index 1):
        Before: [1, 2, 3, 0]   length = 3
        Shift:  [1, 3, 3, 0]   -> arr[1] = arr[2]
        Done:   [1, 3, ?, 0]   -> length becomes 2, arr[2] is now unused
    """
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted.


def printArr(arr, capacity):
    """
    Print every slot in the array, from index 0 to capacity - 1.

    Note: this prints ALL slots (including unused/default ones),
    not just the `length` "real" values — useful for visualizing
    the whole underlying block of memory.
    """
    for i in range(capacity):
        print(arr[i])


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    capacity = 5
    arr = [0] * capacity   # Pre-allocate fixed-size array, all slots default to 0.
    length = 0

    print("Insert 5, 3, 8 at the end:")
    for value in (5, 3, 8):
        insertEnd(arr, value, length, capacity)
        length += 1
    printArr(arr, capacity)   # [5, 3, 8, 0, 0]

    print("\nInsert 9 at index 1 (shifts 3, 8 right):")
    insertMiddle(arr, 1, 9, length)
    length += 1
    printArr(arr, capacity)   # [5, 9, 3, 8, 0]

    print("\nRemove value at index 1 (shifts 3, 8, 0 left):")
    removeMiddle(arr, 1, length)
    length -= 1
    printArr(arr, capacity)   # [5, 3, 8, 0, 0]

    print("\nRemove from the end:")
    removeEnd(arr, length)
    length -= 1
    printArr(arr, capacity)   # [5, 3, 0, 0, 0]
