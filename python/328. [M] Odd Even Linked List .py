class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        dummy_odd_head = ListNode()
        dummy_even_head = ListNode()
        node = head
        odd_node = dummy_odd_head
        even_node = dummy_even_head
        is_odd = True
        while node is not None:
            if is_odd:
                odd_node.next = node
                odd_node = node
            else:
                even_node.next = node
                even_node = node
            is_odd = not is_odd
            node = node.next
        odd_node.next = dummy_even_head.next
        even_node.next = None
        return dummy_odd_head.next
