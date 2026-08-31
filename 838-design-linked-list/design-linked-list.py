class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        current = self.head
        i = 0

        while current:
            if i == index:
                return current.val

            i += 1
            current = current.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = ListNode(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        current = self.head

        for i in range(index - 1):
            current = current.next

        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        current = self.head

        for i in range(index - 1):
            current = current.next

        current.next = current.next.next
        self.length -= 1

#YourMyLinkedListobjectwillbeinstantiatedandcalledassuch:
#obj=MyLinkedList()
#param_1=obj.get(index)
#obj.addAtHead(val)
#obj.addAtTail(val)
#obj.addAtIndex(index,val)
#obj.deleteAtIndex(index)