import java.util.ArrayList;
import java.util.List;

public class Solution199 {
    class Solution {
        public ArrayList list = new ArrayList();

        public List<Integer> rightSideView(TreeNode root) {
            int level = 0;
            Integer value = rightValueLevel(root, level);
            while (value != null){
                list.add(value);
                level++;
                value = rightValueLevel(root,level);
            }

            return list;
        }

        public Integer rightValueLevel(TreeNode node, int level){
            int current_level = 0;

            if (node == null){
                return null;
            }

            if (level == 0){
                return node.val;
            }


            Integer right = rightValueLevel(node.right, level-1);
            Integer left = rightValueLevel(node.left, level-1);

            if (right != null){
                return right;
            }
            else if (left != null){
                return left;
            }

            return null;
        }
    }
}
