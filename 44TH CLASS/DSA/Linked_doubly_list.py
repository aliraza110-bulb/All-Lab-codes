from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None

class DoublyLinked:
    def __init__(self):
        self.head: Optional[Node] = None

    def addATbeggining(self, data: int) -> None:
        new_node = Node(data)  
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node


    def addATEnd(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current


    def insertATPosition(self, index: int, data: int) -> None:
        if index <= 0 or not self.head:
            self.addATbeggining(data) 
            return

        cur = self.head
        pos = 0
        while cur.next and pos < index - 1:
            cur = cur.next
            pos += 1

        node = Node(data)
        node.next = cur.next
        node.prev = cur
        if cur.next:
            cur.next.prev = node
        cur.next = node


    def displayForward(self) -> None:
        cur = self.head
        while cur:
            print(f"{cur.data} -> ", end="")
            cur = cur.next
        print("null")

    def displayBackward(self) -> None:
        cur=self.head
        while cur:
            print(f"{cur.data} -> ",end="")
            cur=cur.prev
        print("null!")

if __name__ == "__main__":
    dll=DoublyLinked()
    for x in [10,20,40]:
        dll.addAtEnd(x)
        print("Input")
        dll.dispalayForward()
        print("Insert 30 at pos=2: ")
        dll.insertATPosition(2,30)
        dll.displayForward()



