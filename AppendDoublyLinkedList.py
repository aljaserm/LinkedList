# next means next address

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def AddNode(self, vals):
        a = Node(vals)
        a.next = self.head
        if self.head is not None:
            self.head.prev = a
        self.head = a

    def insertNode(self, node, vals):
        new = Node(vals)
        new.next = node.next
        node.next = new
        new.prev = node
        if new.next is not None:
            new.next.prev = new

    def appendNode(self, vals):
        new = Node(vals)
        new.next = None
        if self.head is None:
            new.prev = None
            self.head = new
            return
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = new
        new.prev = pointer
        return

    def PrintIt(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next


x = LinkedList()
x.AddNode("MJ")
x.AddNode("OO")
x.AddNode("OJ")
x.AddNode("SJ")
x.AddNode("SM")
x.insertNode(x.head.next, 12)
x.appendNode(20)
x.PrintIt(x.head)
