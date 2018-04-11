import math


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = 0.0
        for i in range(0, len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    area = max(area, self.get_area(
                        points[i], points[j], points[k]))

        return area

    def get_area(self, x, y, z):
        xy = math.sqrt((y[0]-x[0])**2+(y[1]-x[1])**2)
        xz = math.sqrt((z[0]-x[0])**2+(z[1]-x[1])**2)
        yz = math.sqrt((z[0]-y[0])**2+(z[1]-y[1])**2)
        s = (xy+xz+yz)/2
        result = math.sqrt(s*abs((s-xy))*abs((s-xz)*abs((s-yz))))
        # print(result)
        return result


a = Solution().largestTriangleArea([[1, 0], [0, 0], [0, 1]])
print(a)
