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
class Solution {
    public int maxDepth(Node root) {
        
        // DFS
        if(root==null){
            return 0;
        } else if (root.children == null){
            return 1;
        } else {
            int cMax = 0;
            for (Node child:root.children){
                int newValue = maxDepth(child);
                if (newValue > cMax){
                    cMax = newValue;
                }
            }
            return cMax+1;
        }
        
        // BFS
//         if(root == null) return 0;
    
//         Queue<Node> queue = new LinkedList<>();
//         queue.offer(root);

//         int depth = 0;

//         while(!queue.isEmpty())
//         {
//             int size = queue.size();

//             for(int i = 0; i < size; i++)
//             {
//                 Node current = queue.poll();
//                 for(Node child: current.children) queue.offer(child);
//             }

//             depth++;
//         }

//         return depth;
    }
}