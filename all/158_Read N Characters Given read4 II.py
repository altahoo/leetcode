# 158. Read N Characters Given read4 II - Call Multiple Times

# Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        while len(self.queue) < n:
            buf4 = [''] * 4
            read4(buf4)
            self.queue.extend(buf4)
            if not self.queue[-1]:
                break
        
        k = 0
        while self.queue and self.queue[0] and k < n:
            buf[k] = self.queue.popleft()
            k += 1
        
        return k
        