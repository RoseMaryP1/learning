# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
import collections

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


class Point(object):
    visit_grid = [[False for col_items in xrange(len(grid[0]))] for row_items in xrange(len(grid))]

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = None

    def is_visited(self):
        return self.visit_grid[self.row][self.col]

    def visit(self):
        self.visit_grid[self.row][self.col] = True
        return self

    def new_neighbors(self):
        neighbors = []
        for dir in delta:
            row = self.row + dir[0]
            col = self.col + dir[1]
            if row < 0 or col < 0:
                continue
            if row > len(grid) - 1 or col > len(grid[0]) - 1:
                continue
            if grid[row][col] == 1:
                continue
            if self.visit_grid[row][col]:
                continue
            neighbors.append(Point(row, col))
        return neighbors



def compute_value(grid, goal, cost):
    # Create a grid of 99s (what sebastian said we should use, but not sure why)
    value = [[99 for col_items in xrange(len(grid[0]))] for row_items in xrange(len(grid))]
    goal_point = Point(row=goal[0], col=goal[1])
    goal_point.value = 0

    # Breadth first search from goal
    # add goal to the queue as the first item
    todo = collections.deque()
    todo.append(goal_point)

    # while queue not empty
    while len(todo) > 0:

        # pop the first item off the queue as point
        point = todo.popleft().visit()

        # set value of point in the grid
        value[point.row][point.col] = point.value

        # get every neighbor of our point and for each one
        for next_pt in point.new_neighbors():
            # set the value of the neighbor to be point.value + cost
            next_pt.value = point.value + cost
            # add neighbor to the queue
            todo.append(next_pt)

    # return the value grid
    return value

print(compute_value(grid, goal, cost))
