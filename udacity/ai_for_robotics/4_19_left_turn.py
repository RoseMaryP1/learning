# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):

    policy2D = [[' ' for items in xrange(len(grid[0]))] for row in xrange(len(grid))]
    values = [[[999 for items in xrange(len(grid[0]))] for row in xrange(len(grid))] for dir_idx in forward]
    grid_max_row = len(grid) - 1
    grid_max_col = len(grid[0]) -1

    # Try dynamic programming way sine A star might be tricky with variable cost functions.
        # For every direction of travel
    change = True
    round = 1
    while change and round < 10:
        change = False
        round += 1
        print "\nROUND: %d" % (round)
        #print "change = False"

        #print "\nDIR: %s [%d]" % (forward_name[dir_idx], dir_idx)
        # For every position in the grid
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                for dir_idx in xrange(len(forward)):
                    if row == goal[0] and col == goal[1]:
                        if values[dir_idx][row][col] > 0:
                            values[dir_idx][row][col] = 0
                            change = True
                            #print "found goal: Change True"
                    elif grid[row][col] == 0:
                        for a in xrange(len(action)):
                            dir_idx2 = (dir_idx + action[a]) % 4
                            row2 = row + forward[dir_idx2][0]
                            col2 = col + forward[dir_idx2][1]
                            if row2 < 0 or col2 < 0 or row2 > grid_max_row or col2 > grid_max_col:
                                continue
                            if grid[row2][col2] == 1:
                                continue
                            curr_value = values[dir_idx][row][col]
                            move_value = values[dir_idx2][row2][col2]
                            new_value = move_value + cost[a]
                            if new_value < curr_value:
                                #print "(%d, %d) travelling %s: taking action %s puts me at (%d, %d) traveling %s" \
                                #    % (row, col, forward_name[dir_idx], action_name[a], row2, col2, forward_name[dir_idx2])
                                #print "> cost is %d to take action, my cost was %d but is now %d" % \
                                #      (cost[a], values[dir_idx][row][col], new_value)
                                change = True
                                #print "change = True"
                                values[dir_idx][row][col] = new_value
                                #policy2D[row][col] = action_name[a]
    row = init[0]
    col = init[1]
    curr_dir = init[2]
    policy2D[goal[0]][goal[1]] = '*'

    while row != goal[0] or col != goal[1]:
        value = values[curr_dir][row][col]
        lowest = 0
        for a in xrange(len(action)):
            test_dir = (curr_dir + action[a]) % 4
            test_row = row + forward[test_dir][0]
            test_col = col + forward[test_dir][1]
            if test_row < 0 or test_col < 0 or test_row > grid_max_row or test_col > grid_max_col:
                continue
            test_value = values[test_dir][test_row][test_col]

            if value == test_value + cost[a]:
                policy2D[row][col] = action_name[a]
                curr_dir = (curr_dir + action[a]) % 4
                row = row + forward[curr_dir][0]
                col = col + forward[curr_dir][1]
                value = values[curr_dir][row][col]

    #for i in range(len(values)):
    #    print forward_name[i]
    #    for rows in values[i]:
    #        print rows

    return policy2D

print(optimum_policy2D(grid, init, goal, cost))
#for i in range(len(values)):
#    print forward_name[i]
#for row in values:
#    print row
#print "\n"

