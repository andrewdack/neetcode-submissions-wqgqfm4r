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
    int kthVal = -1;
    int cnt = 0;
    int K;
    public int kthSmallest(TreeNode root, int k) {
        K = k;
        inorder(root);
        return kthVal;
    }

    public void inorder(TreeNode root) {
        if (root == null) return;
        if (kthVal != -1) return;
        inorder(root.left);
        cnt++;
        if (cnt == K) {
            kthVal = root.val;
            return;
        }
        inorder(root.right);
    }
}
