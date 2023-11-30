# 170. Two Sum III - Data structure design

# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

# Implement the TwoSum class:

# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.


class TwoSum:

    def __init__(self):
        self.numbers = set()
        self.sums = set()
        

    def add(self, number: int) -> None:
        for num in self.numbers:
            self.sums.add(num + number)
        self.numbers.add(number)

    def find(self, value: int) -> bool:
        return value in self.sums


class TwoSum:

    def __init__(self):
        self.number_freq = collections.defaultdict(int)
        

    def add(self, number: int) -> None:
        self.number_freq[number] += 1

    def find(self, value: int) -> bool:
        for num, freq in self.number_freq.items():
            second = value - num
            if second in self.number_freq:
                if second != num or (second == num and freq > 1):
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)