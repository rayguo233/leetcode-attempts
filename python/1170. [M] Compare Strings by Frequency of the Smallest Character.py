from typing import List
import bisect

CHAR, FREQ = 0, 1

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query_freqs = [self.f(q) for q in queries]  # type: List[int]
        word_freqs = [self.f(w) for w in words]  # type: List[int]
        word_freqs = sorted(word_freqs)
        print(query_freqs)
        print(word_freqs)
        answers = []
        for qf in query_freqs:
            answers.append(len(word_freqs) - bisect.bisect_right(word_freqs, qf))
        return answers

    def f(self, word: str) -> int:
        smallest = [word[0], 0]
        for c in word:
            if smallest[CHAR] < c:
                continue
            elif smallest[CHAR] == c:
                smallest[FREQ] += 1
            else:
                smallest = [c, 1]
        return smallest[FREQ]

if __name__ == '__main__':
    sol = Solution()
    # print(sol.numSmallerByFrequency(['aaaaa'], ['bb', 'bbb', 'aabaaa', 'aabaaaa']))
    print(sol.numSmallerByFrequency(
        ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"],
        ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]))
