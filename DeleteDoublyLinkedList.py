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

    def removeNode(self, node):
        if node.prev is None:
            self.x = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.y = node.prev
        else:
            node.next.prev = node.prev

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
x.removeNode(x.head.next)
x.PrintIt(x.head)
