# 281. Zigzag Iterator

# Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

# Implement the ZigzagIterator class:

# ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# int next() returns the current element of the iterator and moves the iterator to the next element.

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.cur_list = 1
        self.v1 = v1
        self.v2 = v2
        self.cur_i1 = 0
        self.cur_i2 = 0
        

    def next(self) -> int:
        if self.cur_list == 1 and self.cur_i1 < len(self.v1):
            result = self.v1[self.cur_i1]
            self.cur_i1 += 1
            if self.cur_i2 < len(self.v2):
                self.cur_list = 2
            return result
        
        if self.cur_i2 < len(self.v2):
            result = self.v2[self.cur_i2]
            self.cur_i2 += 1
            if self.cur_i1 < len(self.v1):
                self.cur_list = 1
            return result   
         

    def hasNext(self) -> bool:
        return self.cur_i1 < len(self.v1) or self.cur_i2 < len(self.v2)

        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())