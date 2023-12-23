# 251. Flatten 2D Vector

# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

# Implement the Vector2D class:

# Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
# hasNext() returns true if there are still some elements in the vector, and false otherwise.

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = collections.deque([])
        for row in vec:
            if row:
                self.vec.append(collections.deque(row))
        

    def next(self) -> int:
        value = self.vec[0].popleft()
        if not self.vec[0]:
            self.vec.popleft()
        return value
        

    def hasNext(self) -> bool:
        if self.vec:
            return True
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()