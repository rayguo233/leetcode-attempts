import collections
from typing import List


class Solution:

    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        def get_int(w: str) -> int:
            res = 0
            for c in w:
                res |= 1 << (ord(c) - ord('a'))
            return res

        targets = collections.defaultdict(int)
        for target in targetWords:
            targets[get_int(target)] += 1

        res = 0

        for word in startWords:
            word = get_int(word)
            for num in range(26):
                new_word = word | (1 << num)
                if new_word == word:
                    continue
                if new_word in targets:
                    res += targets[new_word]
                    targets[new_word] = 0
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumEvenSplit(6))
    print(sol.maximumEvenSplit(8))
    print(sol.maximumEvenSplit(28))