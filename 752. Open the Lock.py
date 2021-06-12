# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock_failed(self, deadends: list[str], target: str) -> int:
        def inc(char: chr) -> chr:
            if char is None: return None
            if char == '9': return '0'
            return chr(ord(char) + 1)
        def dec(char: chr) -> chr:
            if char is None: return None
            if char == '0': return '9'
            return chr(ord(char) - 1)

        ops = 0
        # for each digit in lock
        for i in range(4):
            up, down = '0', '0'
            bad = [deadend[i] for deadend in deadends]  # type: list[chr]
            while up != target[i] and down != target[i]:
                up, down = inc(up), dec(down)
                if up in bad: up = None
                if down in bad: down = None
                ops += 1
                if up is None and down is None: return -1
        return ops

    def openLock(self, deadends: list[str], target: str) -> int:
        if '0000' in deadends: return -1

        visited = set()
        ops = 0
        stack = ['0000']  # type: list[str]
        next_locks = []

        def inc(lock, i) -> str:
            if lock[i] == '9': return lock[:i] + '0' + lock[i + 1:]
            return lock[:i] + chr(ord(lock[i]) + 1) + lock[i + 1:]

        def dec(lock, i) -> str:
            if lock[i] == '0': return lock[:i] + '9' + lock[i + 1:]
            return lock[:i] + chr(ord(lock[i]) - 1) + lock[i + 1:]

        while stack:
            leng = len(stack)
            for _ in range(leng):
                lock = stack.pop(0)
                if lock == target: return ops
                for i in range(4):
                    next_locks += [inc(lock, i), dec(lock, i)]
                for next_lock in next_locks:
                    if next_lock not in visited and next_lock not in deadends:
                        stack.append(next_lock)
                        visited.add(next_lock)
                next_locks = []
            ops += 1
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    assert(sol.openLock(["0201"], "0202") == 4)
    assert(sol.openLock(["0201"], "0000") == 0)
    assert(sol.openLock(["0202"], "0202") == -1)

    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)