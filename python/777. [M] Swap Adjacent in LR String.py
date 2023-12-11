class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        new_start, new_end = '', ''
        for a, b in zip(start, end):
            if a == b == 'X':
                continue
            new_start += a
            new_end += b

        i, j = 0, 1
        while i < len(start) and j <= len(start):
            si = start[i:j]
            ei = end[i:j]
            # print(si, ei, i, j)
            if si == ei:
                i, j = j, j+1
                continue
            for a, b, char in [(si, ei, 'L'), (ei, si, 'R')]:
                if a[0] == b[-1] == 'X':
                    if not all(c == char for c in a[1:] + b[:-1]):
                        return False
                    i, j = j, j
                    break 
            j += 1
        return i == len(start) 
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.canTransform('RRX', 'XRR'))
    print(sol.canTransform('XLL', 'LLX'))
    print(sol.canTransform('RX', 'XR'))
    print(sol.canTransform('RXXLRXRXL', 'XRLXXRRLX'))
    pass