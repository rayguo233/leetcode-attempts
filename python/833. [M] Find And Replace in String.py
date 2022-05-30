from typing import List


class Solution:

    def findReplaceString(self, s: str, indices: List[int], sources: List[str],
                          targets: List[str]) -> str:
        tuples = sorted([(indices[i], sources[i], targets[i])
                         for i in range(len(indices))])
        prev_end = 0
        res = ''
        for i, src, target in tuples:
            if prev_end < i:
                res += s[prev_end:i]
                prev_end = i
            sub_str_len = len(src)
            if s[i:i + sub_str_len] == src:
                res += target
                prev_end = i + sub_str_len
        res += s[prev_end:]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumEvenSplit(6))
    print(sol.maximumEvenSplit(8))
    print(sol.maximumEvenSplit(28))