/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> nodeList;

        pot(root, nodeList);

        return nodeList;
    }

    void pot(TreeNode* node, vector<int>& nodeList) {
        if (node !=  nullptr) {
            nodeList.push_back(node->val);
            pot(node->left, nodeList);
            pot(node->right, nodeList);
        }
    }
};