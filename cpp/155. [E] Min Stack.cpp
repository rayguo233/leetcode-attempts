#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <stack>

using namespace std;;

class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {}
    
    void push(int val) {
        if (s_.empty())
            return s_.push({val, val});
        s_.push({val, min(val, s_.top().second)});
    }
    
    void pop() {
        s_.pop();
    }
    
    int top() {
        return s_.top().first;
    }
    
    int getMin() {
        return s_.top().second;
    }
private:
    stack<pair<int, int>> s_;
};

int main() {
}