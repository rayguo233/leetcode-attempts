class Solution:

    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_seq = [1]
        a, b = 1, 1
        while a + b <= k:
            a, b = b, a + b
            fib_seq.append(b)
        fib_set = set(fib_seq)
        steps = 1
        if k in fib_set:
            return steps
        needs = {k}
        visited = set()
        while True:
            steps += 1
            next_needs = set()
            for need in needs:
                for fib_num in fib_seq:
                    next_need = need - fib_num
                    if next_need <= 0 or next_need in visited:
                        continue
                    if next_need in fib_set:
                        return steps
                    visited.add(next_need)
                    next_needs.add(next_need)
            needs = next_needs


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinFibonacciNumbers(2))
    print(sol.findMinFibonacciNumbers(4))
    print(sol.findMinFibonacciNumbers(7))
    print(sol.findMinFibonacciNumbers(10))
    print(sol.findMinFibonacciNumbers(19))
    print(sol.findMinFibonacciNumbers(9083494))
