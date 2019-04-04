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

    def begining(self,x4):
        new = Node(x4)
        new.next = self.head
        self.head = new

    def ending(self, x5):
        newer= Node(x5)
        if self.head is None:
            self.head=newer
            return
        lastNode=self.head
        while lastNode.next:
            lastNode= lastNode.next
        lastNode.next=newer

    def Med(self,node,data):
        medNew= Node(data)
        medNew.next=node.next
        node.next=medNew





x = LinkedList()
x.head = Node("MJ")
x2 = Node("OJ")
x3 = Node("MO")

x.head.next = x2
x2.next = x3
x.PrintIt()

x.begining("OO")
print("\n")
x.PrintIt()

x.ending("SJ")
print("\n")
x.PrintIt()

x.Med(x.head.next,"SM")
print("\n")
x.PrintIt()


x.Med(x.head.next.next,"OT")
print("\n")
x.PrintIt()

x.Med(x.head.next.next.next.next,"NP")
print("\n")
x.PrintIt()