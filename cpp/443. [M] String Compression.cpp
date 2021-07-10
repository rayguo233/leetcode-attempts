// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int size = chars.size();
        int prevI = 0;
        char prevC = chars[0];
        int nextI = 0;
        for (int i = 1; i < size; i++) {
            // a different char encountered || same char occuring the 9th time
            if (chars[i] != prevC) {
                chars[nextI] = chars[prevI];
                nextI++;
                if (i - prevI != 1) {
                    int freq = i - prevI;
                    string str = to_string(freq);
                    for (char c : str) {
                        chars[nextI] = c;
                        nextI++;
                    }
                }
                prevI = i;
                prevC = chars[i];
            }
        }
        chars[nextI] = chars[prevI];
        nextI++;
        if (size - prevI > 1) {
            int freq = size - prevI;
            string str = to_string(freq);
            for (char c : str) {
                chars[nextI] = c;
                nextI++;
            }
        }
        return nextI;
    }
};

int main() {
    Solution sol = Solution();
    vector<char> a = {'a','a','b','b','c','c','c'};
    int size = sol.compress(a);
    cout << size << endl;
    for (char c : a) {
        cout << c << ' ';
    }
    cout << endl;
}