# 2.1
# Q: Implement a function to delete duplicate values from a linked list.


class Node(object):
    data = None
    next_ = None # type: Node

    def __init__(self, data):
        self.data = data

    def __str__(self):
        output = str(self.data)
        n = self
        while n.next_ is not None:
            n = n.next_
            output += str(n.data)
        return output

    def append(self, data):
        tail = Node(data)
        n = self
        while n.next_ is not None:
            n = n.next_
        n.next_ = tail
        return self


def remove_dupes(first_node):
    """
    Args:
        first_node (Node)
    """
    items = set(first_node.data)
    n = first_node
    while n.next_ is not None:
        if n.next_.data in items:
            n.next_ = n.next_.next_
        else:
            items.add(n.next_.data)
            n = n.next_

if __name__ == '__main__':

    list1 = Node("A").append("B").append("C").append("C").append("A")
    print(str(list1))

    remove_dupes(list1)

    print(str(list1))
