class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Merge_Lists:
    def min_idx(self, lists):
        idx = 0

        for i in range(len(lists)):
            if lists[i].val < lists[idx].val:
                idx = i
        return idx

    def merge_k(self, lists):
        head = tail = ListNode(-1)

        lists = list(filter(lambda x: x is not None, lists))

        while len(lists) > 0:
            min_idx = self.min_idx(lists)

            tail.next = lists[min_idx]
            tail = tail.next
            lists[min_idx] = lists[min_idx].next

            if lists[min_idx] is None:
                del lists[min_idx]

        return head.next

list1 = ListNode(1)
list1.next = ListNode(3)
list2 = ListNode(2)
list2.next = ListNode(4)
s = Merge_Lists()

x = s.merge_k([list1, list2])
print(x.val)
print(x.next.val)
print(x.next.next.val)
print(x.next.next.next.val)
# print(x.next.next.next.next.val)