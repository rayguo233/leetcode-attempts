# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

# You are given a perfect binary tree where all leaves
# are on the same level, and every parent has two
# children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right
# node. If there is no next right node, the next pointer
# should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


MAX_HEIGHT = 12


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        rights = [None] * MAX_HEIGHT  # type: list[Node]

        def proc_children(node: Node, depth: int) -> None:
            if node.left is None:
                return

            node.left.next = node.right
            if rights[depth] is not None:
                rights[depth].next = node.left
            rights[depth] = node.right

            proc_children(node.left, depth+1)
            proc_children(node.right, depth+1)

        proc_children(root, 0)
        return root

    def connect_1(self, root: 'Node') -> 'Node':
        queue = [root]
        while queue[0] is not None:
            leng = len(queue)
            prev = None
            for _ in range(leng):
                curr = queue.pop(0)
                queue += [curr.left, curr.right]
                if prev is not None:
                    prev.next = curr
                prev = curr
        return root


if __name__ == '__main__':
    sol = Solution()
    # print(sol.invertTree([2,1,4]))
    # assert(sol.invertTree([1,2,1,2]) == 1)
