"""
DYNAMIC ARRAY - TUTORIAL
=========================

A dynamic array is an array that can GROW as more elements are added,
unlike a static array which has a fixed capacity forever.

Python's built-in `list` is already dynamic — but this file builds one
from scratch (on top of a fixed-size list) so you can see HOW that
"automatic growing" actually works under the hood.

Same two tracked numbers as the static array:
    - capacity -> total slots currently allocated (can change over time).
    - length   -> number of slots holding "real" data (length <= capacity).

The key idea: whenever the array fills up (length == capacity), we
don't just add one more slot — we allocate a whole NEW, bigger array
(commonly double the capacity), copy everything over, and discard the
old one. This "resize" is expensive, but it happens rarely, so the
*average* cost of adding an element stays cheap. This is called
amortized O(1) insertion.
"""


class Array:
    def __init__(self):
        """
        Start small: capacity of 2, and no real elements yet.

        arr = [0, 0]   <- 2 reserved slots, both placeholders
        length = 0     <- none of them are "real" data yet
        """
        self.capacity = 2
        self.length = 0
        self.arr = [0] * self.capacity  # Array of capacity = 2

    def pushback(self, n):
        """
        Insert value `n` at the end of the array.

        Time complexity: amortized O(1)
            - Usually O(1): just write to arr[length].
            - Occasionally O(n): when a resize is triggered.
            - Averaged over many pushes, the cost works out to O(1) each.

        Steps:
            1. If the array is completely full (length == capacity),
               grow it first by calling resize().
            2. Place `n` in the next open slot (arr[length]).
            3. Increment length, since we now have one more real value.
        """
        if self.length == self.capacity:
            self.resize()

        # Insert at next empty position.
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        """
        Double the array's capacity.

        Time complexity: O(n)
            - Every existing element has to be copied into the new array.

        Why double instead of adding a fixed amount (e.g. +1)?
            - If we only grew by 1 slot each time, we'd have to resize
              (and copy everything) on EVERY single insert -> O(n) per
              insert, O(n^2) total for n inserts.
            - Doubling means resizes happen less and less often as the
              array grows, so the total copying work across all inserts
              stays proportional to n (not n^2) -> amortized O(1) per insert.

        Steps:
            1. Compute the new capacity (2x the old one).
            2. Allocate a brand new array of that size (filled with
               placeholder 0s).
            3. Copy every existing "real" element (0 .. length-1) from
               the old array into the new one, at the same indices.
            4. Replace the old array reference with the new one.

        Example:
            Before: arr = [1, 2]        capacity = 2, length = 2
            After:  arr = [1, 2, 0, 0]  capacity = 4, length = 2 (unchanged)
        """
        # Create new array of double capacity.
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # Copy elements to newArr.
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def popback(self):
        """
        Remove the last element of the array.

        Time complexity: O(1)

        Note: unlike the static array version, we don't bother
        overwriting arr[length - 1] with a default value here — we
        simply shrink `length` by 1. The old value is still physically
        sitting in the array, but since it's now beyond `length`, it's
        treated as "not real" and will just get overwritten the next
        time pushback() is called.
        """
        if self.length > 0:
            self.length -= 1

    def get(self, i):
        """
        Return the value at index `i`.

        Time complexity: O(1)

        Steps:
            1. Check `i` is within the "real" data range (i < length).
               (We deliberately don't check against capacity — indices
               at or beyond length are considered out of bounds even if
               the underlying array physically has room there.)
            2. Return arr[i] if valid, otherwise raise an IndexError.
        """
        if i < self.length:
            return self.arr[i]
        # Here we would throw an out of bounds exception.
        raise IndexError("Index out of bounds")

    def insert(self, i, n):
        """
        Overwrite the value at index `i` with `n`.

        Time complexity: O(1)

        Note: despite the name, this does NOT shift elements like
        insertMiddle did for the static array — it simply replaces
        whatever is already at index `i`. It only works on indices that
        already hold real data (i < length); it can't be used to append
        past the end (use pushback() for that).
        """
        if i < self.length:
            self.arr[i] = n
            return
        # Here we would throw an out of bounds exception.
        raise IndexError("Index out of bounds")

    def print(self):
        """
        Print every "real" value in the array, from index 0 to length - 1.

        Unlike printArr() in the static array example, this only prints
        the meaningful values — not the unused/placeholder slots beyond
        length (even though those slots still physically exist up to
        capacity).
        """
        for i in range(self.length):
            print(self.arr[i])
        print()


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    dynamic_arr = Array()
    print(f"Initial capacity: {dynamic_arr.capacity}")   # 2

    print("\nPush back 1, 2, 3 (3rd push triggers a resize):")
    for value in (1, 2, 3):
        dynamic_arr.pushback(value)
        print(f"  pushed {value} -> capacity: {dynamic_arr.capacity}, length: {dynamic_arr.length}")
    dynamic_arr.print()   # 1  2  3

    print("get(1):", dynamic_arr.get(1))   # 2

    print("\ninsert(0, 99):")
    dynamic_arr.insert(0, 99)
    dynamic_arr.print()   # 99  2  3

    print("popback():")
    dynamic_arr.popback()
    dynamic_arr.print()   # 99  2
