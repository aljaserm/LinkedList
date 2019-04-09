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
x.PrintIt(x.head)
