from collections import deque
from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        id_to_indx = {}
        for i, e in enumerate(employees):
            id_to_indx[e.id] = i
        dq = deque([id])
        res = 0
        while dq:
            curr_id = dq.popleft()
            curr_e = employees[id_to_indx[curr_id]]
            res += curr_e.importance
            dq += curr_e.subordinates
        return res






if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses('()'))
    print(sol.scoreOfParentheses('(())'))
    print(sol.scoreOfParentheses('(()()())'))
    print(sol.scoreOfParentheses('(())()()'))
    print(sol.scoreOfParentheses('((()()))'))
