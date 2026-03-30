class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_points = []
        for point in points:
            x, y = point
            dist = x*x + y*y
            dist_points.append((dist, point))
        dist_points.sort(key=lambda x: x[0])
        ans = []
        for i in range(k):
            ans.append(dist_points[i][1])
        return ans