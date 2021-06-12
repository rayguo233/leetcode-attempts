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

    def openLock_better(self, deadends: list[str], target: str) -> int:
        visited1 = set('0000')
        visited2 = set()
        visited2.add(target)
        ops = 0
        stack1 = ['0000']  # type: list[str]
        stack2 = [target]  # type: list[str]
        next_locks = []

        if '0000' in deadends or target in deadends: return -1

        def inc(lock, i) -> str:
            if lock[i] == '9': return lock[:i] + '0' + lock[i + 1:]
            return lock[:i] + chr(ord(lock[i]) + 1) + lock[i + 1:]

        def dec(lock, i) -> str:
            if lock[i] == '0': return lock[:i] + '9' + lock[i + 1:]
            return lock[:i] + chr(ord(lock[i]) - 1) + lock[i + 1:]

        while stack1 or stack2:
            leng = len(stack1)
            for _ in range(leng):
                lock = stack1.pop(0)
                if lock in visited2: return ops
                for i in range(4):
                    next_locks += [inc(lock, i), dec(lock, i)]
                for next_lock in next_locks:
                    if next_lock not in visited1 and next_lock not in deadends:
                        stack1.append(next_lock)
                        visited1.add(next_lock)
                next_locks = []
            if leng > 0: ops += 1
            stack1, stack2 = stack2, stack1
            visited1, visited2 = visited2, visited1
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    assert(sol.openLock_better(["0201"], "0202") == 4)
    assert(sol.openLock_better(["0201"], "0000") == 0)
    assert(sol.openLock_better(["0202"], "0202") == -1)

    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)