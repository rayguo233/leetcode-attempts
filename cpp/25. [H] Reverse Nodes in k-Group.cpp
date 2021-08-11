#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <stack>

using namespace std;;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0, head);
        ListNode *ptr = &dummy;
        while (true) {
            stack<ListNode*> s;
            ListNode *start = ptr;
            while (ptr->next && s.size() < k) {
                s.push(ptr->next);
                ptr = ptr->next;
            }
            if (s.size() < k)
                return dummy.next;
            ptr = ptr->next;
            while (!s.empty()) {
                start->next = s.top();
                s.pop();
                start = start->next;
            }
            start->next = ptr;
            ptr = start;
        }
        assert(false);
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}