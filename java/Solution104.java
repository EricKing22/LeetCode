import com.sun.source.tree.Tree;

public class Solution104 {
    public int maxDepth(TreeNode root){

        if (root == null) return 0;

        int left = 1, right = 1;

        if (root.left != null){
            left  += maxDepth(root.left);
        }
        if (root.right != null){
            right += maxDepth(root.right);
        }



        return Math.max(left, right);


    }
}
