#3.4 : Implement towers of hanoi program using stacks.


class Stack(object):

    def __str__(self):
        output = ""
        for i in self.data:
            output += str(i) + "->"
        return output

    def __init__(self):
        self.data = list()
        self.top = None

    def __len__(self):
        return len(self.data)

    def push(self, x):
        self.data.append(x)
        if self.top is None:
            self.top = 0
        else:
            self.top += 1
        return self

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        if self.top is 0:
            self.top = None
        else:
            self.top -= 1
        return self.data.pop()

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.data[self.top]


def move(_towers, _from, _to, _temp, height):
    if height == 1:
        # Move the base
        _towers[_to].push(towers[_from].pop())
        return
    else:
        height -= 1

        # Move all the previous items to the temp tower.
        move(_towers, _from, _temp, _to, height)

        # Move the base
        _towers[_to].push(towers[_from].pop())

        # Move temp to destination
        move(_towers, _temp, _to, _from, height)

if __name__ == '__main__':
    t1 = Stack()
    t2 = Stack()
    t3 = Stack()
    t1.push(3).push(2).push(1).push(0)

    towers = [t1, t2, t3]
    height = len(t1)
    move(towers, 0, 2, 1, height)

    print(str(towers[2]))

def create_tour(nodes):
    """

    :param nodes:
    :return:
    """
    nodes = list()
    start = nodes.pop()
    prev = start
    paths = []
    for n in nodes:
        paths.append((prev, n))
        prev = n
    paths.append((prev, start))
    if test(paths):
        #print "PASS"
    else:
        #print "FALSE"
    return paths


