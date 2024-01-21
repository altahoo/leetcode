# 313. Super Ugly Number

# A super ugly number is a positive integer whose prime factors are in the array primes.

# Given an integer n and an array of integers primes, return the nth super ugly number.

# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        queue = [1]
        while n > 1:
            n -= 1
            num = heapq.heappop(queue)
            for prime in primes:
                heapq.heappush(queue, num * prime)
                if num % prime == 0:
                    break
        return queue[0]