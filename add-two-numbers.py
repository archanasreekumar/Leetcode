https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list=[]
        l2_list=[]
        while l1:
            l1_list.append(l1.val)
            l1=l1.next
        while l2:
            l2_list.append(l2.val)
            l2=l2.next
        l1_list=l1_list[::-1]
        l2_list=l2_list[::-1]
        l1_int=int("".join(map(str,l1_list)))
        l2_int=int("".join(map(str,l2_list)))
        out_int=l1_int+l2_int
        node=ListNode(0)#main head node
        current=node# copy of main head node to modify in loop
        for i in str(out_int)[::-1]:
            current.next=ListNode(int(i))# head --> 1st int and so on
            current=current.next# 1st int made the current head so that it can point in next (1st-->2nd)
        return node.next