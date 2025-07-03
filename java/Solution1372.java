import com.sun.source.tree.Tree;

public class Solution1372 {

    class Solution{
        public int maxLength = 0;


        public int longestZigZag(TreeNode root){

            solve(root,0,0);
            solve(root,1,0);

            return maxLength;

        }

        public void solve(TreeNode node, int direction, int currentLength){

            if(currentLength > maxLength) maxLength = currentLength;

            if (direction == 1 && node.right != null){
                solve(node.right, 0, 1+currentLength);
                solve(node.right, 1, 0);
            }
            else if (direction == 0 && node.left != null){
                solve(node.left, 1, 1+currentLength);
                solve(node.left,0,0);
            }
            else{
                return;
            }

        }
    }
}
