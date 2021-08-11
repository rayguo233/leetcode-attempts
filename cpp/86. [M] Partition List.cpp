// https://leetcode.com/problems/group-anagrams/

#include <vector>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode less = ListNode(), more = ListNode();
        ListNode *less_ptr = &less, *more_ptr = &more;
        while (head) {
            if (head->val < x) {
                less_ptr->next = head; less_ptr = head;

            }
            else {
                more_ptr->next = head; more_ptr = head;
            } 
            head = head->next;
        }
        if (more_ptr)
            more_ptr->next = nullptr;
        if (!(less.next))
            return more.next;
        // cout << more.next->val << endl;
        less_ptr->next = more.next;
        // cout << less.next->val << endl;
        return less.next;
    }
};