from typing import List
from collections import deque, defaultdict

END_OF_WORD = 'A'

class StreamChecker:

    def __init__(self, words: List[str]):
        self.ptrs = []
        self.root = {}
        for word in words:
            curr_node = self.root
            for char in word:
                if char not in curr_node:
                    curr_node[char] = {}
                curr_node = curr_node[char]
            curr_node[END_OF_WORD] = {}

    def query(self, letter: str) -> bool:
        self.ptrs = [node[letter] for node in self.ptrs + [self.root] if letter in node]
        return any(END_OF_WORD in node for node in self.ptrs)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

if __name__ == '__main__':
    s = StreamChecker(['abc', 'abb', 'ab', 'a', 'b'])
    print(s.root)
    print(s.root['a'])
    print(s.query('a'))
    print(s.query('b'))
    print(s.query('c'))