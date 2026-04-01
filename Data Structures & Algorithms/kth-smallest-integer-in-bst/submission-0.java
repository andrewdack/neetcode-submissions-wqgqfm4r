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
    public int kthSmallest(TreeNode root, int k) {
        ArrayList<Integer> nodes = new ArrayList<Integer>();
        inOrderAddNodesToArray(root, nodes);
        return nodes.get(k - 1);
    }   

    public void inOrderAddNodesToArray(TreeNode root, List nodes) {
        if (root != null) {
            inOrderAddNodesToArray(root.left, nodes);
            nodes.add(root.val);
            inOrderAddNodesToArray(root.right, nodes);
        }
    }
}
