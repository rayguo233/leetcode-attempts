from typing import List, Tuple

DIR = [(0, 1), (-1, 0), (0, -1), (1, 0)]
Pos = Tuple[int, int]
Line = Tuple[Pos, Pos]
DEFAULT_LINE = ((10**6,10**6), (10**6,10**6))  # type: Line
X, Y = 0, 1

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        def is_crossing(line1_start: Pos, line1_end: Pos, line2_start: Pos, line2_end: Pos) -> bool:
            def swap_x_y(p: Pos) -> Pos:
                return (p[1], p[0])
            if (line1_start[X] == line1_end[X] and line2_start[X] == line2_end[X]):
                return line1_start[X] == line2_start[X] and\
                    any(min(line1_start[Y], line1_end[Y]) <= line2_y <= max(line1_start[Y], line1_end[Y]) for line2_y in [line2_start[Y], line2_end[Y]])
            if (line1_start[Y] == line1_end[Y] and line2_start[Y] == line2_end[Y]):
                return line1_start[Y] == line2_start[Y] and \
                    any(min(line1_start[X], line1_end[X]) <= line2_x <= max(line1_start[X], line1_end[X]) for line2_x in [line2_start[X], line2_end[X]])
            if line1_start[Y] == line1_end[Y]:
                line1_start = swap_x_y(line1_start)
                line1_end = swap_x_y(line1_end)
                line2_start = swap_x_y(line2_start)
                line2_end = swap_x_y(line2_end)
            line1_x = line1_start[X]
            line2_y = line2_start[Y]
            print(line1_x, line2_y, line1_start, line1_end, line2_start, line2_end)
            return (((line2_start[X] <= line1_x <= line2_end[X]) or (line2_end[X] <= line1_x <= line2_start[X]))
                        and 
                    (min(line1_start[Y], line1_end[Y]) <= line2_y <= max(line1_start[Y], line1_end[Y])))

        sides = [DEFAULT_LINE] * 4 # type: List[Line]
        curr_pos = (0, 0)
        prev_line = DEFAULT_LINE
        for i, d in enumerate(distance):
            i %= 4
            next_pos = (curr_pos[0] + DIR[i][0] * d, curr_pos[1] + DIR[i][1] * d)
            for line_start, line_end in sides:
                if is_crossing(curr_pos, next_pos, line_start, line_end):
                    print(curr_pos, next_pos, line_start, line_end)
                    return True
            sides[(i+3)%4] = prev_line
            prev_line = (curr_pos, next_pos)
            curr_pos = next_pos
            print(curr_pos)
        return False


        
if __name__ == '__main__':
    sol = Solution()
    print(sol.isSelfCrossing(distance = [2,1,1,2]))
    print(sol.isSelfCrossing(distance = [1,2,3,4]))
    print(sol.isSelfCrossing(distance = [1,1,1,1]))
    print(sol.isSelfCrossing(distance = [1,1,2,1,1]))
    pass