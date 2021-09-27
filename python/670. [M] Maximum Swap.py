

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        max_digits = [[s[-1], len(s)-1]]
        for i in range(len(s)-1, -1, -1):
            if ord(s[i]) > ord(max_digits[-1][0]):
                max_digits.append([s[i], i])
        for i, d in enumerate(s):
            if i == max_digits[-1][1]:
                max_digits.pop()
                continue
            if ord(d) < ord(max_digits[-1][0]):
                s = s[:i] + max_digits[-1][0] + s[i+1:max_digits[-1][1]] + d + s[max_digits[-1][1] + 1:]
                return int(s)

        return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSwap(387161))
