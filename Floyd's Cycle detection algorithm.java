In Floyd’s cycle detection algorithm (Tortoise and Hare):

We detect a cycle when slow and fast point to the exact same node in memory, not just when their values match.
  public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {  // Compare nodes, not values
                return true;
            }
        }
        return false;
    }
}
