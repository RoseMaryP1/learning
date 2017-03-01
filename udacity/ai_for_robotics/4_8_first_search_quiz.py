# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import collections

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

expand_list = []


class Point(object):

    def __init__(self, row, col, cost=0, visited=False):
        self.row = row
        self.col = col
        self.cost = cost

def expand(grid, point, visited, cost):
    global delta
    new_points = []
    for move in delta:
        row = move[0] + point.row
        col = move[1] + point.col
        if row < 0 or col < 0:
            continue
        if row > len(grid) - 1 or col > len(grid[0]) - 1:
            continue
        if (row, col) in visited:
            continue
        if grid[row][col] == 1:
            continue
        new_points.append(Point(row, col, cost=point.cost+cost))
    return new_points


def search(grid, init, goal, cost):
    open_list = collections.deque()
    visited = []
    goal = Point(goal[0], goal[1])

    # If we start on a one, fail.
    if grid[init[0]][init[1]] == 1:
        return "fail"
    # Create a new point and add to the open list.
    open_list.append(Point(init[0], init[1], 0))

    while len(open_list) > 0:
        p = open_list.popleft()
        visited.append((p.row, p.col))
        if p.row  == goal.row and p.col == goal.col:
            return [p.cost, p.row, p.col]
        for n in expand(grid, p, visited, cost):
            open_list.append(n)

    return "fail"

print(search(grid, init, goal, cost))
