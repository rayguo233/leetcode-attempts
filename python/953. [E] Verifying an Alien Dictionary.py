# https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly they also use english
# lowercase letters, but possibly in a different order. The
# order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language,
# and the order of the alphabet, return true if and only if
# the given words are sorted lexicographicaly in this alien
# language.
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

class Solution:
    def isW1BeforeW2(self, w1, w2, d):
        len1, len2 = len(w1), len(w2)
        i = 0
        while i < len1 and i < len2:
            if d[w1[i]] < d[w2[i]]: return True
            if d[w1[i]] > d[w2[i]]: return False
            i += 1
        assert(i == min(len1, len2))
        return len1 <= len2


    def isAlienSorted(self, words: list[str], order: str) -> bool:
        d = dict()
        for i, c in enumerate(order):
            d[c] = i

        prev = words[0]
        for w in words[1:]:
            if not self.isW1BeforeW2(prev, w, d): return False
            prev = w

        return True

if __name__ == '__main__':
    sol = Solution()
    # print(sol.getLine(['i', 'ride', 'bus'], curr_width=10, maxWidth=17))
    print(sol.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
    # print(sol.merge([[1,2]]))
    # print(sol.merge([[1,2]]))
    # print(sol.merge_try2([[1,2],[0,9],[6,7]]))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
