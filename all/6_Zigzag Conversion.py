# 6. Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lists = [[] for i in range(numRows)]
        row = 0
        direction = 1
        for char in s:
            lists[row].append(char)
            row += direction
            if direction == 1 and row == numRows:
                direction = -1
                row = numRows - 2
            elif direction == -1 and row == -1:
                direction = 1
                row = 1
        return ''.join([''.join(row) for row in lists])