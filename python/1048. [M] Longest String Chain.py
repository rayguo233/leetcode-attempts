import collections
from typing import List


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        word_to_chain_len = {w: 1 for w in words}
        res = 1
        for word in words:
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred not in word_to_chain_len:
                    continue
                word_to_chain_len[word] = max(word_to_chain_len[pred] + 1,
                                              word_to_chain_len[word])
            res = max(res, word_to_chain_len[word])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('abaacbbca'))
    print(sol.removeDuplicateLetters('abadddacbddbc'))