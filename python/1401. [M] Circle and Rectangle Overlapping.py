class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        '''
        scenarios:
            - circle touching or covering vertical or horizontal lines
            - circle touching or including rectangle corners
        '''
        # check if corner is covered:
        for x, y in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
            if ((x - xCenter) ** 2 + (y - yCenter) ** 2) <= radius ** 2:
                return True
        # check if vertial line is covered
        if (y1 <= yCenter <= y2) and any(xCenter-radius <= x <= xCenter+radius for x in [x1, x2]):
            return True
        # check if horizontal line is covered
        if (x1 <= xCenter <= x2) and any(yCenter-radius <= y <= yCenter+radius for y in [y1, y2]):
            return True
        # check if the whole circle is insider rectangle
        return (y1 <= yCenter < y2) and (x1 <= xCenter <= x2)



if __name__ == '__main__':
    s = Solution()
    print(s.checkOverlap(1, 0, 0, -2,-2,2,2))
