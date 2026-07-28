#include <print> 
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;

        vector<int> columns(n, 0);
        vector<int> diag1(2*n - 1, 0);
        vector<int> diag2(2*n - 1, 0);

        vector<string> boardList(n, string(n, '.'));

        backTrack(0, n, boardList, res, columns, diag1, diag2);
        return res;
    }


    void backTrack(int r, int n, vector<string>& boardList, vector<vector<string>>& res, vector<int>& columns, vector<int>& diag1, vector<int>& diag2) {
        if (r == n) {
            res.push_back(boardList);
            return;
        }

        for (int c = 0; c < n; c++) {
            if (columns[c] || diag1[r + c] || diag2[c - r + n - 1]) continue;

            columns[c] = diag1[r + c] = diag2[c - r + n - 1] = 1;
            editBoard(boardList, r, c, "Q");

            backTrack(r + 1, n, boardList, res, columns, diag1, diag2);

            columns[c] = diag1[r + c] = diag2[c - r + n - 1] = 0;
            editBoard(boardList, r, c, ".");
        } 

    }


    void editBoard(vector<string>& boardList, int r, int c, const string& newVal) {
        string oldVal = boardList[r];
        boardList[r] = oldVal.substr(0, c) + newVal + oldVal.substr(c + 1);
    }
};
