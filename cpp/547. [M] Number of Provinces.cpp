#include <vector>
#include <algorithm>
#include <iostream>
#include <assert.h>
#include <string>
#include <memory>
#include <unordered_set>

using namespace std;;

struct Union {
    unique_ptr<int[]> m_parent;
    int size;
    
    Union(int n) : m_parent{new int[n]}, size{n} {
        for (int i = 0; i < n; i++) {
            m_parent[i] = i;
        }
    }

    void connect(int child, int parent) {
        child = find(child);
        parent = find(parent);
        m_parent[child] = parent;
    }

    int find(int child) {
        while (m_parent[child] != child) {
            m_parent[child] = m_parent[m_parent[child]];
            child = m_parent[child];
        }
        return child;
    }   

    int findNumProv() {
        unordered_set<int> m;
        for (int i = 0; i < size; i++) {
            int p = m_parent[i];
            while (p != m_parent[p]) {
                p = m_parent[p];
            }
            if (m.find(p) == m.end()) {
                m.insert(p);
            }
        }
        return m.size();
    }
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int size = isConnected.size();
        Union u(size);
        for (int i = 0; i < size; i++) {
            int parent = -1;
            for (int j = 0; j < size; j++) {
                if (isConnected[i][j] == 0)
                    continue;
                if (parent == -1)
                    parent = j;
                u.connect(j, parent);
                cout << "connect " << j << ' ' << parent << endl;
            }
        }
        return u.findNumProv();
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> v = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
    sol.findCircleNum(v);
}