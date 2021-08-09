#include <vector>
#include <unordered_map>
#include <assert.h>
#include <iostream>
#include <queue>
#include <set>

using namespace std;;

class Window {
public:
    Window(int k) : k_is_odd_(k % 2) {}

    void Insert(int x) {
        Trim();
        assert(lower_size_ <= upper_size_);
        if (lower_size_ == upper_size_ && (lower_size_ == 0 || lower_.top() <= x)) {
            upper_size_++;
            return upper_.push(x);
        }
        if (lower_size_ == upper_size_)
            return ShiftAdd(true, x);
        if (x <= upper_.top()) {
            lower_size_++;
            return lower_.push(x);
        }
        return ShiftAdd(false, x);
    }

    void Erase(int x) {
        Trim();
        cout << x << ":" << upper_.size() << endl;
        assert(lower_size_ <= upper_size_);
        assert(upper_size_);
        if (upper_.top() == x) {
            upper_size_--;
            upper_.pop();
            return Balance();
        }
        assert(lower_size_);
        if (lower_.top() == x) {
            lower_size_--;
            lower_.pop();
            return Balance();
        }
        num_to_freq_[x]++;
        if (x > upper_.top()) {
            upper_size_--;
            return Balance();
        }
        lower_size_--;
        Balance();
    }

    double GetMid() {
        Trim();
        if (k_is_odd_)
            return upper_.top();
        cout << lower_.top() << ":" << upper_.top() << endl;
        return ((double)upper_.top() + lower_.top()) / 2.0;
    }
private:
    priority_queue<int> lower_;
    priority_queue<int, vector<int>, greater<int>> upper_;
    int lower_size_ = 0;
    int upper_size_ = 0;
    unordered_map<int, int> num_to_freq_;
    bool k_is_odd_;
    void Trim() {
        while (lower_size_ > 0 && (num_to_freq_[lower_.top()] || num_to_freq_[upper_.top()])) {
            if (num_to_freq_[lower_.top()]) {
                num_to_freq_[lower_.top()]--;
                lower_.pop();
                Balance();
                continue;
            } 
            if (num_to_freq_[upper_.top()]) {
                num_to_freq_[upper_.top()]--;
                upper_.pop();
                Balance();
            }
        }
    }
    void Balance() {
        if (lower_size_ > upper_size_)
            Shift(true);
        else if (lower_size_+1 < upper_size_)
            Shift(false);
    }
    void Shift(bool low_to_up) {
        Trim();
        if (low_to_up) {
            upper_.push(lower_.top());
            lower_.pop();
            lower_size_--;
            upper_size_++;
        } else {
            lower_.push(upper_.top());
            upper_.pop();
            upper_size_--;
            lower_size_++;
        }
    }
    void ShiftAdd(bool low_to_up, int x) {
        Shift(low_to_up);
        if (low_to_up) {
            lower_.push(x);
            lower_size_++;
        } else {
            upper_.push(x);
            upper_size_++;
        }
    }
};

class Solution {
public:
    vector<double> medianSlidingWindow_failed(vector<int>& nums, int k) {
        vector<double> res;
        Window w(k);
        for (int i = 0; i < k; i++)
            w.Insert(nums[i]);
        for (int i = k; i < nums.size(); i++) {
            cout << nums[i] << endl;
            res.push_back(w.GetMid());
            w.Erase(nums[i-k]);
            w.Insert(nums[i]);
        }
        res.push_back(w.GetMid());
        return res;
    }
};

int main() {
    unordered_map<int, int> m;
    vector<int> v = {1,4,2,3};
    Solution sol = Solution();
    auto res = sol.medianSlidingWindow_failed(v, 4);
    for (double n : res) {
        cout << " " << n;
    }
    
}