class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int m = nums.size() / 2;

        while (l <= r) {
            int item = nums[m];

            if (target == item) {
                return m;
            }
            if (target < item) {
                r = m - 1;
            }
            if (target > item) {
                l = m + 1;
            }
            m = (r + l) / 2;
        }
        return -1;
    }
};
