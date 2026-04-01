class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> h = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (h.containsKey(nums[i])) {
                System.out.println(nums[i] + " exists in the map.");
                return true;
            }
            else h.put(nums[i], 0);
        }
        return false;
    }
}
