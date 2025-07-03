import java.util.Stack;

public class Solution206 {
    class ListNode {

        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }


    class Solution{
        public ListNode reverseList(ListNode head) {
            Stack<ListNode> stack = new Stack<>();

            ListNode current = head;
            while (current != null) {
                stack.add(current);
                current = current.next;
            }

            if(stack.isEmpty()) return null;

            ListNode newHead = stack.pop();
            current = newHead;

            while (!stack.isEmpty()) {
                current.next = stack.pop();
                current = current.next;
            }

            current.next = null;


            return newHead;
        }

    }

}
