from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        def c_to_i(c: str) -> int:
            return ord(c) - ord('a')
        w_len = len(words[0])
        # record frequencies
        freq = [[0] * 26 for _ in range(w_len + 1)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][c_to_i(char)] += 1
        # find result
        dp, next_dp = [1] * (w_len + 1), [0] * (w_len + 1)
        for char in reversed(target):
            for i in reversed(range(w_len)):
                letter_freq = freq[i]
                next_dp[i] = letter_freq[c_to_i(char)] * dp[i+1] + next_dp[i+1]
            dp, next_dp = next_dp, [0] * (w_len + 1)
        return dp[0] % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.getLine(['i', 'ride', 'bus'], curr_width=10, maxWidth=17))
    print(sol.numWays(words = ["acca","bbbb","caca"], target = "aba"))
    print(sol.numWays(words = ["abba","baab"], target = "bab"))
    # print(sol.merge([[1,2]]))
    # print(sol.merge([[1,2]]))
    # print(sol.merge_try2([[1,2],[0,9],[6,7]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
