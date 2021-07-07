# https://leetcode.com/problems/text-justification/

# Given an array of words and a width maxWidth, format the
# text such that each line has exactly maxWidth characters and
# is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is,
# pack as many words as you can in each line. Pad extra
# spaces ' ' when necessary so that each line has exactly
# maxWidth characters.
#
# Extra spaces between words should be distributed as evenly
# as possible. If the number of spaces on a line do not
# divide evenly between words, the empty slots on the left
# will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified
# and no extra space is inserted between words.
#
# Note:
#
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

class Solution:

    def getLine(self, words, curr_width, maxWidth) -> str:
        if len(words) == 1: return words[0] + ' ' * (maxWidth - len(words[0]))
        l = words[0]
        num_space = len(words) - 1
        base_extra = (maxWidth - curr_width) // num_space
        offset = (maxWidth - curr_width) % num_space
        for i, w in enumerate(words[1:]):
            l += ' ' * (base_extra + 1)
            if i < offset: l += ' '
            l += w
        return l

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        curr_width = len(words[0])
        stack = [words[0]]
        for w in words[1:]:
            if curr_width + 1 + len(w) > maxWidth:
                lines.append(self.getLine(stack, curr_width, maxWidth))
                stack = [w]
                curr_width = len(w)
                continue
            stack.append(w)
            curr_width += 1 + len(w)
        last_line = ''
        for w in stack:
            if not last_line:
                last_line = w
            else:
                last_line += ' ' + w
        lines.append(self.getLine([last_line], curr_width, maxWidth))
        return lines


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
