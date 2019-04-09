# next means next address

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def PrintIt(self):
        printed = self.head
        while printed is not None:
            print(printed.data)
            printed = printed.next


    def DeletingNode(self, DeleteNode):
        new = self.head
        if new is not None:
            if new.data == DeleteNode:
                self.head = new.next
                new = None
                return

        while new is not None:
            if new.data == DeleteNode:
                break
            prev = new
            new = new.next

        if new is None:
            return

        prev.next = new.next
        new = None


x = LinkedList()
x.head = Node("MJ")
x2 = Node("OJ")
x3 = Node("MO")
x4 = Node("OO")

x.head.next = x2
x2.next = x3
x3.next = x4
x.PrintIt()
print("\n")
x.DeletingNode("OJ")
x.PrintIt()
