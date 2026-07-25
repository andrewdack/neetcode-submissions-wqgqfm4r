class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;
        backtrack(0, nums, subset, res);
        return res;
    }

    void backtrack(int i, vector<int>& nums, vector<int>& subset, vector<vector<int>>& res) {
        if (i == nums.size()) {
            res.push_back(subset);
            return;
        }
        int val = nums[i];
        subset.push_back(val);
        backtrack(i + 1, nums, subset, res);

        subset.pop_back();
        backtrack(i + 1, nums, subset, res);


    }
};
