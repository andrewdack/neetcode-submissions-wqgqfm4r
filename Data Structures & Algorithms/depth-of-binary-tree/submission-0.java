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
    // do a depth first search 
    public int maxDepth(TreeNode root) {
        return maxHelper(root, 0);
    }

    public static int maxHelper(TreeNode root, int maxSum) {
        if (root == null) {
            return 0;
        }
        
        int leftTree = maxHelper(root.left, maxSum);
        int rightTree = maxHelper(root.right, maxSum);
        int best = Math.max(leftTree, rightTree);

        maxSum = 1 + best;
        return maxSum;
    }
}
