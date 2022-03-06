import bisect
import collections
import heapq
import sys
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter

IMPOS = 1000

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [IMPOS] * time
        for start, end in clips:
            if time <= start:
                continue
            prev = dp[start - 1] if start else 0
            if prev == IMPOS:
                continue
            for i in range(start, min(end, time)):
                dp[i] = min(dp[i], prev + 1)
            # print(start, end, dp)
        if dp[time-1] == IMPOS: return -1
        return dp[time-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10))
    print(sol.videoStitching(clips = [[0,5],[6,8]], time = 7))
    # print(sol.nthSuperUglyNumber([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
