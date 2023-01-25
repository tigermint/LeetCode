# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = node = ListNode(0)
        l1_prev = l1; l2_prev = l2
        tmp = 0
       
        while l1_prev and l2_prev:
            prev.val = l1_prev.val + l2_prev.val + tmp
            tmp = 0            
            if prev.val >= 10:
                tmp = prev.val // 10
                prev.val = prev.val % 10
            # 다음 
            l1_prev = l1_prev.next
            l2_prev = l2_prev.next
            prev.next = ListNode(0)
            prev = prev.next
        while l1_prev:
            
            prev.val = l1_prev.val + tmp
            tmp = 0
            if prev.val >= 10:
                tmp = prev.val // 10
                prev.val = prev.val % 10
            
            # 다음 
            l1_prev = l1_prev.next
            prev.next = ListNode(0)
            prev = prev.next
        
        while l2_prev:
            prev.val = l2_prev.val + tmp
            tmp = 0
            if prev.val >= 10:
                tmp = prev.val // 10
                prev.val = prev.val % 10
            # 다음 
            l2_prev = l2_prev.next
            prev.next = ListNode(0)
            prev = prev.next
            
        # 끝 자리
        if tmp != 0:
            prev.val = tmp
            tmp = 0
        cur = node
        while cur and prev.val == 0:
            print(cur)
            if cur.next.next == None:
                cur.next = None
                break
            cur = cur.next
        return node
        
            
            
        