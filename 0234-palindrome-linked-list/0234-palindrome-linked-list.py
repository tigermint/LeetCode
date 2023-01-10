# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        node_list = []      
        while node.next:
            node_list.append(node.val)
            node = node.next
        node_list.append(node.val)
        
        left, right = 0, len(node_list) - 1
        while left < right:
            if node_list[left] != node_list[right]:
                return False
            left += 1; right -=1
        return True 
        
            