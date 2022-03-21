"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def process(ss: str, ni: NestedInteger) -> str:
            if not ss:
                return
            this_level = NestedInteger()
            ni.add(this_level)
            ss = ss[1:]
            while ss[0] != ']':
                if ss[0] == ',':
                    ss = ss[1:]
                if ss[0] == '[':
                    ss = process(ss, this_level)
                    continue
                i = 0
                while ss[i] == '-' or ss[i].isnumeric():
                    i += 1
                this_level.add(NestedInteger(int(ss[:i])))
                ss = ss[i:]
            return ss[1:]

        if s[0] != '[':
            return NestedInteger(int(s))
        l = NestedInteger()
        process(s, l)
        return l.getList()[0]
        