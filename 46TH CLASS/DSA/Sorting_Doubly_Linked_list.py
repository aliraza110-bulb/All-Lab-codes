from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None


    def addAtEnd(self, data: int) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.prev = cur


    def displayForward(self) -> None:
        cur = self.head
        while cur:
            print(f"{cur.data} -> ", end="")
            cur = cur.next
        print("null")


    def _insert_into_sorted(self, sorted_head: Optional[Node], node: Node) -> Optional[Node]:
        if sorted_head is None:
            node.prev = node.next = None
            return node
        if node.data <= sorted_head.data:
            node.next = sorted_head
            node.prev = None
            sorted_head.prev = node
            return node
        cur = sorted_head
        while cur.next and cur.next.data < node.data:
            cur = cur.next
        node.next = cur.next
        node.prev = cur
        if cur.next:
            cur.next.prev = node
        cur.next = node
        return sorted_head


    def sort(self) -> None:
        sorted_head: Optional[Node] = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.prev = cur.next = None
            sorted_head = self._insert_into_sorted(sorted_head, cur)
            cur = nxt
        self.head = sorted_head


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for x in [40, 20, 30, 10]:
        dll.addAtEnd(x)
    print("Input:")
    dll.displayForward()
    dll.sort()
    print("Sorted:")
    dll.displayForward()