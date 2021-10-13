from typing import List
from collections import defaultdict, deque
import itertools

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        d = defaultdict(set)
        steps = [float('inf')] * len(arr)
        for i, num in enumerate(arr):
            d[num].add(i)
        steps[0] = 0
        curr_level = deque([0])
        visited, visited_groups = set(), set()
        visited.add(0)
        while curr_level:
            curr_level_len = len(curr_level)
            for _ in range(curr_level_len):
                i = curr_level.popleft()  # type: int
                i_step = steps[i]  # type: float
                for next_i in itertools.chain([i+1, i-1]):
                    if next_i in visited or not 0 <= next_i < len(arr):
                        continue
                    visited.add(next_i)
                    curr_level.append(next_i)
                    steps[next_i] = i_step + 1
                    if next_i == len(arr) - 1:
                        return int(steps[next_i])
                if arr[i] in visited_groups:
                    continue
                for next_i in itertools.chain(d[arr[i]]):
                    if next_i in visited or not 0 <= next_i < len(arr):
                        continue
                    visited.add(next_i)
                    curr_level.append(next_i)
                    steps[next_i] = i_step + 1
                    if next_i == len(arr) - 1:
                        return int(steps[next_i])
                visited_groups.add(arr[i])

if __name__ == '__main__':
    sol = Solution()
    print(sol.minJumps([1]))
    print(sol.minJumps([7,6,9,6,9,6,9,7]))
    print(sol.minJumps([6,1,9]))
    print(sol.minJumps([11,22,7,7,7,7,7,7,7,22,13]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
