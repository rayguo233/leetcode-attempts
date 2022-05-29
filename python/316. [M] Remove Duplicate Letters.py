import heapq


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        c_to_last_i = {}
        for i, c in enumerate(s):
            c_to_last_i[c] = i
        stack = []
        for i, char in enumerate(s):
            if char in stack:
                continue
            while stack and c_to_last_i[stack[-1]] > i and char < stack[-1]:
                stack.pop()
            stack.append(char)
        return ''.join(stack)

    def removeDuplicateLetters_version0(self, s: str) -> str:
        c_to_last_i = {}
        for i, c in enumerate(s):
            c_to_last_i[c] = i
        last_chars = sorted([(val, key) for key, val in c_to_last_i.items()])
        res = ''
        start_i = 0
        # print(last_chars)
        for last_i, char in last_chars:
            if char in res:
                continue
            while start_i <= last_i and char not in res:
                sub_str = s[start_i:last_i + 1]
                # print(sub_str, '---')
                heap = list(sub_str)
                heapq.heapify(heap)
                while heap and heap[0] in res:
                    heapq.heappop(heap)
                if not heap:
                    start_i = last_i + 1
                    break
                sub_str_min_char = heap[0]
                sub_str_min_char_i = sub_str.index(sub_str_min_char) + start_i
                res += sub_str_min_char
                start_i = sub_str_min_char_i + 1
                # print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('abaacbbca'))
    print(sol.removeDuplicateLetters('abadddacbddbc'))