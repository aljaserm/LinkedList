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
    # def begining(self):
    #     new= Node(x4)


x = LinkedList()
x.head = Node("MJ")
x2 = Node("OJ")
x3 = Node("MO")

x.head.next = x2
x2.next = x3
x.PrintIt()


