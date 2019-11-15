class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cusor_now = 0
        l3 = ListNode(0)
        l4 = ListNode(0)
        init = 0
        while l2 != None:
            if init == 0:
                l3 = ListNode((l1.val + l2.val + cusor_now) % 10)
                l4 = l3
                init = 1
            else:
                l4.next = ListNode((l1.val + l2.val +cusor_now) % 10)
                l4 = l4.next
            cusor_now = (l1.val + l2.val) // 10
            l2 = l2.next
            l1 = l1.next
            if l1 == None:
                l1 = ListNode(0)
        print(l3,'              ',l4)
        l4 = l3
        print(l3,'              ',l4)
        if cusor_now == 1:
            print(l3,l4)
            l4.next = ListNode((l1.val + 1) % 10)
            l4 = l4.next
            if (l1.val + 1) // 10 == 0:
                print(l3,l4)
                return l3
            else:
                l4.next = ListNode((l1.val + 1) // 10)
                l4 = l4.next
                print(l3,l4)
                return l3