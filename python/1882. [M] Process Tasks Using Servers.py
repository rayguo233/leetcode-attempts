import heapq
from typing import List


class Solution:

    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free_server_hp = [(w, i) for i, w in enumerate(servers)]
        busy_server_hp = []
        heapq.heapify(free_server_hp)
        ans = [0] * len(tasks)
        for i, time in enumerate(tasks):
            curr_time = i
            while busy_server_hp and busy_server_hp[0][0] <= i:
                _, server_w, server_i = heapq.heappop(busy_server_hp)
                heapq.heappush(free_server_hp, (server_w, server_i))
            if not free_server_hp:
                curr_time, server_w, server_i = heapq.heappop(busy_server_hp)
                heapq.heappush(free_server_hp, (server_w, server_i))
            server_w, server_i = heapq.heappop(free_server_hp)
            ans[i] = server_i
            heapq.heappush(busy_server_hp,
                           (curr_time + time, server_w, server_i))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.new21Game(6, 1, 10))