class node:
    def __init__(self,data:int):
        self.data=data
        self.left=None
        self.right=None
    class binarysearchtree:
        def __init__(self):
            self.root=None
        def insert(self,value,:int) -> None:
            if self.root is None:
                self.root=node(value)
            else:
                self.insert_recursive(self.root,value)
        def _insert_recursive(self,node:Node,value:int)-> None
        if value<node.data:
            if node.left is None:
                node.left=node(value)
            else:
                self._insert_recursive(node,left,value)
        else:
            if node.right is None