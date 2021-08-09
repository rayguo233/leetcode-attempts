#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>

using namespace std;;

class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {

    }
    
    void addNum(int num) {
        int lower_size = lower_.size(), upper_size = upper_.size();
        if (lower_size == upper_size)
            return lower_.push(num);
        if (upper_size == 0 && lower_.top() <= num)
            return upper_.push(num);
        if (upper_size == 0) {
            upper_.push(lower_.top());
            lower_.pop();
            return lower_.push(num);
        }
        
    }
    
    double findMedian() {

    }
private:
    priority_queue<int> lower_;
    priority_queue<int, vector<int>, greater<int>> upper_;
};

int main() {

}