import collections
from lib2to3.pytree import WildcardPattern
from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        word_len = len(beginWord)
        word_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                word_dict[word[:i] + '_' + word[i + 1:]].append(word)

        visited = ({beginWord}, {endWord})
        to_dfs = [collections.deque([beginWord]), collections.deque([endWord])]
        curr_terminal = 0
        num_steps = 0

        while to_dfs[0] or to_dfs[1]:
            if not to_dfs[curr_terminal]:
                curr_terminal = not curr_terminal
                continue

            num_steps += 1
            curr_to_dfs = to_dfs[curr_terminal]
            curr_visited = visited[curr_terminal]
            curr_level_size = len(curr_to_dfs)

            for _ in range(curr_level_size):
                word = curr_to_dfs.popleft()
                for i in range(word_len):
                    wild_card = word[:i] + '_' + word[i + 1:]
                    if wild_card not in word_dict:
                        continue
                    for next_word in word_dict[wild_card]:
                        if next_word in curr_visited:
                            continue
                        if next_word in visited[not curr_terminal]:
                            return num_steps
                        curr_visited.add(next_word)
                        curr_to_dfs.append(next_word)

            curr_terminal = not curr_terminal

        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.ladderLength('abc', 'cvu', ['asd', 'avc', 'cvc', 'cvu']))