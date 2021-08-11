// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

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
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head);
        ListNode *ptr = &dummy;
        while (ptr->next && ptr->next->next) {
            ListNode *close = ptr->next, *far = ptr->next->next;
            close->next = far->next;
            ptr->next = far;
            ptr->next->next = close;
            far->next = close;
            ptr = close;
        }
        return dummy.next;
    }
};

int main() {
    Solution sol = Solution();
    vector<int> input = {1,2,3,4,5,6,7};
    vector<int> ::iterator ptr;
}