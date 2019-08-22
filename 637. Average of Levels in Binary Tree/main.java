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
    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> listTreeNode = new LinkedList<TreeNode>();
        List<Double> result = new ArrayList<>();
        if (root == null) return result;
        listTreeNode.add(root);
            
        while (!listTreeNode.isEmpty()){
            int breadth = listTreeNode.size();
            double sum = 0.0;
            // use stream is much slower
            // result.add(listTreeNode.stream().mapToDouble(o->o.val).sum()/breadth);
            for (int i=0;i<breadth;++i ){
                TreeNode node = listTreeNode.poll();
                sum += node.val;
                if (node.left !=null){
                    listTreeNode.offer(node.left);
                }
                if (node.right != null){
                    listTreeNode.offer(node.right);
                }
            }
            result.add(sum/breadth);
            
        }
        return result;
    }
}