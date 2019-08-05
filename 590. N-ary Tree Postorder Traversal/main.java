/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
// Recursion Method
// class Solution {
//     List<Integer> list = new ArrayList<Integer>();
//     public List<Integer> postorder(Node root) {
//         if (root == null)
//             return list;
        
//         for(Node node: root.children)
//             postorder(node);
        
//         list.add(root.val);
        
//         return list;
//     }
// }

// Iteration Method
class Solution {
    List<Integer> result = new ArrayList<Integer>();
    public List<Integer> postorder(Node root) {
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
        if(root==null) return result;
        while (!stack.empty()){
            root = stack.pop();
            result.add(root.val);
            for (Node node:root.children){
                stack.push(node);
            }
        }
        Collections.reverse(this.result);
        return result;
    }
}