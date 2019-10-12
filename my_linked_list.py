class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


node_1 = Node('e')
node_2 = Node('d', node_1)
node_3 = Node('c', node_2)
node_4 = Node('b', node_3)
head = Node('a', node_4)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def read(self, index):
        # We do not assign self.head to theNode
        # because range(0, -1) is a valid expression.
        theNode = None
        for i in range(0, index):
            if i == 0:
                theNode = self.head
            if theNode is None:
                return None
            theNode = theNode.next

        if theNode is None:
            return None

        return theNode.val


linked_list = LinkedList(head)
print(linked_list.read(1))
