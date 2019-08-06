/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        // method 1
        if (root==null) return 0;
        if(root.val <L){
            return rangeSumBST(root.right,L,R);
        }
        if (root.val >R){
            return rangeSumBST(root.left,L,R);
        }
        return root.val+rangeSumBST(root.left,L,R)+rangeSumBST(root.right,L,R);
        
        // method 2
        // if (root==null) return 0;
        // else {
        //     return (L<=root.val && root.val<=R ? root.val:0) + rangeSumBST(root.left,L,R) + rangeSumBST(root.right,L,R);
        // }
    }
}