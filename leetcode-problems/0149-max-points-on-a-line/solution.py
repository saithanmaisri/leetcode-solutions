import math
from functools import reduce

class Solution(object):
    def maxPoints(self, points):
        def gcd(a, b):
            return gcd(b % a, a) if a != 0 else b

        if not points:
            return 0
        if len(points) <= 2:
            return len(points)

        pointsInLine = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                # line: ax + by + c = 0
                if x1 == x2:
                    # equation: x = x1
                    a, b, c = 1, 0, -x1
                else:
                    a, b, c = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
                # make sure a is positive
                if a < 0:
                    a, b, c = -a, -b, -c
                # get gcd of a, b and c
                g = reduce(gcd, (a, b, c)) if a or b or c else 1 #handle the case when a,b,c are all 0.
                # reduce fraction
                a, b, c = a / g, b / g, c / g
                line = (a, b, c)
                pointsInLine.setdefault(line, set())
                pointsInLine[line].add(i)
                pointsInLine[line].add(j)
        # edge case: return 0 for 0 point, 1 for 1 point
        return max(map(len, pointsInLine.values())) if pointsInLine else len(points)
