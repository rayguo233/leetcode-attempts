// https://leetcode.com/problems/copy-list-with-random-pointer/

#include <vector>  
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head)
            return nullptr;
        unordered_map<Node*, int> ntoi;
        unordered_map<int, Node*> iton;
        Node *dummy = new Node(0);
        Node *prev = dummy, *curr;
        int i = 0;
        // construct new list
        while (head) {
            curr = new Node(head->val);
            curr->random = head->random;
            prev->next = curr;
            ntoi[head] = i;
            iton[i] = curr;
            prev = curr;
            head = head->next;   
            i++;         
        }
        // fill in random pointer
        curr = dummy->next;
        i = 0;
        while (curr) {
            if (curr->random) {
                curr->random = iton[ntoi[curr->random]];
            }
            curr = curr->next;
        }
        // return result
        return dummy->next;
    }
};

int main() {
    Solution sol = Solution();
}