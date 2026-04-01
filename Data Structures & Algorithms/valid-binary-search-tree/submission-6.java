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
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        else if (root.left == null && root.right == null ) {
            return true;
        }
        else if (root.left == null) {
            return root.right.val > root.val && root.val < min(root.right) && isValidBST(root.right);
        }
        else if (root.right == null) {
            return root.left.val < root.val && root.val > max(root.left) && isValidBST(root.left);
        }


        return (root.right.val > root.val && root.left.val < root.val &&
                root.val > max(root.left) && root.val < min(root.right) &&
                isValidBST(root.left) && isValidBST(root.right));
    }

    public int min(TreeNode root) {
        int min = root.val;
        while (root != null){
            min = root.val;
            root = root.left;
        }
        return min;
    }

    public int max(TreeNode root) {
        int max = root.val;
        while (root != null) {
            max = root.val;
            root = root.right;
        }
        return max;
    }
}
