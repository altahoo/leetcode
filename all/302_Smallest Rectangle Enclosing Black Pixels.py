# 302. Smallest Rectangle Enclosing Black Pixels

# You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

# The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

# Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# You must write an algorithm with less than O(mn) runtime complexity

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        queue = collections.deque([(x, y)])
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0
        while queue:
            cur_x, cur_y = queue.popleft()
            min_x = min(min_x, cur_x)
            min_y = min(min_y, cur_y)
            max_x = max(max_x, cur_x)
            max_y = max(max_y, cur_y)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = cur_x + i, cur_y + j
                if 0 <= next_x < len(image) and 0 <= next_y < len(image[0]) and image[next_x][next_y] == '1':
                    image[next_x][next_y] = '0'
                    queue.append((next_x, next_y))
        return (max_x - min_x + 1) * (max_y - min_y + 1)