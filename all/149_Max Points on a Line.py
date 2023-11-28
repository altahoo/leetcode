# 149. Max Points on a Line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()
        result = 0
        n = len(points)

        for i in range(n):
            slopes = []
            for j in range(i + 1, n):
                if (points[j][0] - points[i][0]) == 0:
                    slopes.append("No")
                else:
                    slopes.append((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]))
            
            if slopes:
                test_list = Counter(slopes)
                result = max(result, test_list.most_common(1)[0][1])
        
        return result + 1
