
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(val=101, next=head)
        node = dummy
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                while node.next.next and node.next.next.val == node.next.val:
                    node.next.next = node.next.next.next
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
