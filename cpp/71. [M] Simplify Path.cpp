// https://leetcode.com/problems/container-with-most-water/

#include <vector>  
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        int size = path.size();
        if (size < 2)
            return path;
        int writeStrPtr = 1, readStrPtr = 1;
        // jump through '/'s
        while (readStrPtr < size && path.at(readStrPtr) == '/') {
            readStrPtr++;
        }
        //
        while (readStrPtr < size) {
            assert(path.at(readStrPtr) != '/');
            assert(writeStrPtr <= readStrPtr);
            // get next directory name: path[readStrPtr, readStrPtr + nextDirLen]
            int nextDirLen = 1;
            while (readStrPtr + nextDirLen < size && path.at(readStrPtr+nextDirLen) != '/') {
                nextDirLen++;
            }
            string nextDir = path.substr(readStrPtr, nextDirLen);
            cout << "nextDit: " << nextDir << endl;
            // process next dir name
            if (nextDir == "..") {
                if (writeStrPtr >= 2) {
                    writeStrPtr -= 2;
                    assert(path.at(writeStrPtr+1) == '/');
                    // jump through previous dir
                    while (path.at(writeStrPtr-1) != '/')
                        writeStrPtr--;
                }
            } else if (nextDir != ".") {
                path.replace(writeStrPtr, nextDirLen, nextDir);
                path[writeStrPtr + nextDirLen] = '/';
                writeStrPtr += nextDirLen + 1;
            }
            readStrPtr += nextDirLen;
            // jump through '/'s
            while (readStrPtr < size && path.at(readStrPtr) == '/') {
                readStrPtr++;
            }
        }
        // if (writeStrPtr > 2)
        //     writeStrPtr -= 2;
        if (writeStrPtr > 1 && writeStrPtr-1 < size && path.at(writeStrPtr-1) == '/')
            writeStrPtr -= 1;
        if (writeStrPtr < size)
            path.resize(writeStrPtr);
        return path;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.simplifyPath("/...") << endl;
    cout << sol.simplifyPath("/...") << endl;
    // cout << sol.simplifyPath("") << endl;
    // cout << sol.simplifyPath("/") << endl;
    // cout << sol.simplifyPath("//") << endl;
    // cout << sol.simplifyPath("/12///") << endl;
    // cout << sol.simplifyPath("/12") << endl;
    // cout << sol.simplifyPath("//12///") << endl;
    // cout << sol.simplifyPath("/1/2/3/") << endl;
    // cout << sol.simplifyPath("/..") << endl;
    // cout << sol.simplifyPath("/../../../") << endl;
    // cout << sol.simplifyPath("/.././../") << endl;
    // cout << sol.simplifyPath("/.") << endl;
}