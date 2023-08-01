# 223. Rectangle Area

# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        if any([
            bx2 <= ax1,
            bx1 >= ax2,
            by2 <= ay1,
            by1 >= ay2
        ]):
            return area1 + area2
        
        return area1 + area2 - (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1))