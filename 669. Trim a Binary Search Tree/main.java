/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    int L, R;

    public TreeNode trimBST(TreeNode root, int L, int R) {
        this.L = L;
        this.R = R;
        return trim(root);
    }

    private TreeNode trim(TreeNode node) {
        if (node == null) {
            return null;
        } else if (node.val < L) {
            return trim(node.right);
        } else if (node.val > R) {
            return trim(node.left);
        } else {
            node.left = trim(node.left);
            node.right = trim(node.right);
        }
        return node;
    }
}