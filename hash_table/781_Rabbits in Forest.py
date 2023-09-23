# 781. Rabbits in Forest

# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

# Given the array answers, return the minimum number of rabbits that could be in the forest

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        number_to_rabbits = {}
        for ans in answers:
            number = ans + 1
            if number not in number_to_rabbits or number_to_rabbits[number] == 0:
                result += number
                number_to_rabbits[number] = number - 1
            else:
                number_to_rabbits[number] -= 1
        return result