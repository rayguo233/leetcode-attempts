// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>

using namespace std;;

class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() { }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        sstack_.push_back(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (squeue_.empty()) {
            Transfer();
        }
        int back = squeue_.back();
        squeue_.pop_back();
        return back;

    }
    
    /** Get the front element. */
    int peek() {
        if (squeue_.empty()) {
            Transfer();
        }
        return squeue_.back();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return sstack_.empty() && squeue_.empty();
    }
private:
    vector<int> sstack_;
    vector<int> squeue_;
    void Transfer() {
        assert(squeue_.empty() && !sstack_.empty());
        while (!sstack_.empty()) {
            int back = sstack_.back();
            sstack_.pop_back();
            squeue_.push_back(back);
        }
    }
};

int main() {
}