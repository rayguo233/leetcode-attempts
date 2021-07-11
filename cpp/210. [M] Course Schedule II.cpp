// https://leetcode.com/problems/two-sum/

#include <vector>
#include <unordered_set>
#include <assert.h>
#include <iostream>

using namespace std;;

#define C 0
#define R 1

struct Node {
    int m_course;
    int m_numReq;
    vector<int> m_reqFor;

    Node() : m_numReq(0) {}

    void add(int reqFor) {
        m_reqFor.push_back(reqFor);
    }
};

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        Node courses[numCourses];
        unordered_set<int> noReq;
        for (int i = 0; i < numCourses; i++) {
            courses[i].m_course = i;
            noReq.insert(i);
        }
        // construct graph
        for (vector<int> v : prerequisites) {
            Node *req, *cour;
            // get cour
            cour = &courses[v[C]];
            (cour->m_numReq)++;
            if (cour->m_numReq == 1 && noReq.find(v[C]) != noReq.end()) {
                noReq.erase(v[C]);
            }
            // get req
            req = &courses[v[R]];
            req->add(v[C]);
            // cout << req->m_reqFor.size() << req->m_course << &req << endl;
        }
        // construct path
        vector<int> res;
        while (!noReq.empty()) {
            Node *cour = &(courses[*(noReq.begin())]);
            // cout << cour->m_course << courses[0].m_reqFor.size() << cour << endl;
            noReq.erase(cour->m_course);
            res.push_back(cour->m_course);
            numCourses--;
            for (int reqFor : cour->m_reqFor) {
                // cout << reqFor << endl;
                (courses[reqFor].m_numReq)--;
                if (courses[reqFor].m_numReq == 0) {
                    noReq.insert(courses[reqFor].m_course);
                }
            }
        }
        if (numCourses != 0) {
            return {};
        }
        // return result
        return res;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0}};
    auto vec = sol.findOrder(2, v);
    for (auto i : vec) {
        cout << i << ' ';
    }
    cout << endl;
}