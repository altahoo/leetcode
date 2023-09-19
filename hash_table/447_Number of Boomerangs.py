# 447. Number of Boomerangs

# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Return the number of boomerangs.

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):
            dist_points = collections.defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                a = points[i][0] - points[j][0]
                b = points[i][1] - points[j][1]
                dist_points[a * a + b * b] += 1
            
            for num in dist_points.values():
                if num >= 2:
                    result += num * (num - 1)
        return result