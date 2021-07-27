#include <vector>  
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int containVirus(vector<vector<int>> &isInfected) {
        int nrows = isInfected.size();
        int ncols = isInfected.at(0).size();
        int walls_built = 0;
        vector<int[2]> next_round_cells;
        return -1;
    }
        // first round of infection
//         int max_infected = 0;
//         int ignore_cell[2];
//         unordered_set<int[2]> max_backtrack;
//         for (int r = 0; r < nrows; r++) {
//             for (int c = 0; c < ncols; c++) {
//                 isin
//             }
//         }
//         walls_built += max_infected;
//         backtrack_infection(isInfected, max_backtrack);
        
//         // continue further rounds of infection
//         while (!next_round_cells.empty()) {
//             for (int[2] cell : next_round_cells) {
//                 if (cell[0] == ignore_cell[0] && cell[1] == ignore_cell[1]) {
//                     ignore_cell = {-1, -1}; // only ignore once
//                     continue;
//                 }

//             }
//         }

//         return walls_built;
//     }
// private:
//     void infect_wrapper(vector<vector<int>> &isInfected, unordered_set<int[2]> &max_backtrack, int ignore_cell[2],
//         int &max_infected, const int &nrows, const int &ncols, const int &r, const int &c)
//     {
//         unordered_set<int[2]> curr_backtrack;
//         int curr_infected = infect_recursive(isInfected, max_backtrack, curr_backtrack, nrows, ncols, r, c);
//         assert(curr_infected != max_infected || curr_infected == 0);
//         if (curr_infected > 0)
//             next_round_cells.push_back(*(curr_backtrack.begin()));
//         if (curr_infected > max_infected) {
//             ignore_cell[0] = (*(curr_backtrack.begin()))[0];
//             ignore_cell[1] = (*(curr_backtrack.begin()))[1];
//             max_infected = curr_infected;
//             swap(curr_backtrack, max_backtrack);
//         }
//     }

//     int infect_recursive(vector<vector<int>> &isInfected, unordered_set<int[2]> &max_backtrack,
//         unordered_set<int[2]> &curr_backtrack, const int &nrows, const int &ncols, const int &r, const int &c)
//     {

//     }

//     void backtrack_infection(vector<vector<int>> &isInfected, unordered_set<int[2]> &max_backtrack) {

//     }
};

int main() {
    return 1;
}