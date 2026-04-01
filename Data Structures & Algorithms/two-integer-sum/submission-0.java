class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> m = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (m.containsKey(difference)) {
                res[0] = m.get(difference);
                res[1] = i;
                break;
            } else {
                m.put(nums[i], i);
            }
        }
        return res;
    }
}
