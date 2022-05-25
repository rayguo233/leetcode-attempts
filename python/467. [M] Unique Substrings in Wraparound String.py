import collections


class Solution:

    def findSubstringInWraproundString(self, p: str) -> int:
        start, end = 0, 0
        record = collections.defaultdict(int)
        while start < len(p):
            while end + 1 < len(p) and self.are_neighbors(p[end], p[end + 1]):
                end += 1
            self.record_substring(p[start], end - start + 1, record)
            start = end + 1
            end = start
        return sum(record.values())

    def record_substring(self, first_char: str, length: int,
                         record: dict) -> None:
        for dist in range(min(length, 26)):
            curr_char = chr((ord(first_char) + dist - ord('a')) % 26 +
                            ord('a'))
            # print(curr_char)
            record[curr_char] = max(length - dist, record[curr_char])

    def are_neighbors(self, first: str, second: str) -> bool:
        return (ord(first) == ord(second) - 1) or (first == 'z'
                                                   and second == 'a')


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstringInWraproundString('aca'))
    print(sol.findSubstringInWraproundString('zab'))
    sol.record_substring('z', 2, collections.defaultdict(int))
    sol.record_substring('a', 2, collections.defaultdict(int))
