// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class TripleInOne {
public:
    TripleInOne(int stackSize) : stack_size_(stackSize), stack_(stackSize*3, -1) {
        
    }
    
    void push(int stackNum, int value) {
        if (ptr_[stackNum] == stack_size_)
            return;
        stack_.at(ptr_[stackNum] * 3 + stackNum) = value;
        ptr_[stackNum]++;
    }
    
    int pop(int stackNum) {
        if (ptr_[stackNum] == 0)
            return -1;
        ptr_[stackNum]--;
        return stack_.at(ptr_[stackNum] * 3 + stackNum);
    }
    
    int peek(int stackNum) {
        if (ptr_[stackNum] == 0)
            return -1;
        return stack_.at((ptr_[stackNum]-1) * 3 + stackNum);
    }
    
    bool isEmpty(int stackNum) {
        return ptr_[stackNum] == 0;
    }
private:
    int stack_size_;
    vector<int> stack_;
    int ptr_[3] = {0, 0, 0};
};