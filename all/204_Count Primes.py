# 204. Count Primes

# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    def countPrimes(self, n: int) -> int:

        def _factors(n):
            result = []
            for i in range(1, n + 1):
                if n % i == 0:
                    result.append(i)
            return result
        
        def _is_prime(n):
            return n >= 2 and _factors(n) == [1, n]
        
        result = 0
        for i in range(2, n):
            if _is_prime(i):
                result += 1
        return result


class Solution:
    def countPrimes(self, n: int) -> int:
      result = 0
      is_prime = [True] * n
      for i in range(2, n):
        if not is_prime[i]:
          continue
        result += 1
        j = 2
        while i * j < n:
          is_prime[i * j] = False
          j += 1
      return result