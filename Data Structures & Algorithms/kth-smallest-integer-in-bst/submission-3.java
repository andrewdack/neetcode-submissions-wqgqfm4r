/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    // do a in order traversal to store all the nodes in an array
    // index the k - 1 element
    int kthVal = 0;
    int cnt = 0;
    public int kthSmallest(TreeNode root, int k) {
        helper(root, k);
        return kthVal;
    }

    public void helper(TreeNode root, int target) {
        if (root == null) {
        }
        else {
            helper(root.left, target);
            cnt++;
            System.out.println(root.val + " " + cnt);
            if (cnt == target) {kthVal = root.val;}
            helper(root.right, target);
        }
    }
}
