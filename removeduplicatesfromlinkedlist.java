83. Remove Duplicates from Sorted List
Solved
Easy
Topics
premium lock iconCompanies

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
   ListNode temp = head;
        
        while (temp != null && temp.next != null) {
            if (temp.val == temp.next.val) {
                // Skip the duplicate node
                temp.next = temp.next.next;
            } else {
                temp = temp.next;
            }
        }
        
        return head;
    }
}
