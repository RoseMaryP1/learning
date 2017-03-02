# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']  # Use these when creating your policy grid.


# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------


def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    failure_prob = (1.0 - success_prob) / 2.0  # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    wrong_actions = [[0, -1], [0, 1], # when up: left + right
                     [1, 0], [0,1], # when left: down + up
                     [1, 0], [0, 1], # when up: left + right
                     [1, 0], [0, 1]] # when up: left + right

    changed = True
    value[goal[0]][goal[1]] = 0
    policy[goal[0]][goal[1]] = '*'

    def is_collision(pt):
        if pt[0] < 0 or pt[0] > len(grid) - 1 or pt[1] < 0 or pt[1] > len(grid[0]) - 1:
            return True
        if grid[pt[0]][pt[1]] == 1:
            return True
        return False

    while changed:
        changed = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if is_collision([row,col]):
                     continue
                for i in range(len(delta)):

                    l_i = (i + 1) % 4
                    r_i = (i - 1) % 4

                    main = [row + delta[i][0], col + delta[i][1]]
                    left = [row + delta[l_i][0], col + delta[l_i][1]]
                    right = [row + delta[r_i][0], col + delta[r_i][1]]

                    val = cost_step
                    if is_collision(main):
                        val += collision_cost * success_prob
                    else:
                        val += value[main[0]][main[1]] * success_prob

                    if is_collision(left):
                        val += collision_cost * failure_prob
                    else:
                        val += value[left[0]][left[1]] * failure_prob

                    if is_collision(right):
                        val += collision_cost * failure_prob
                    else:
                        val += value[right[0]][right[1]] * failure_prob

                    if val < value[row][col]:
                        value[row][col] = val
                        policy[row][col] = delta_name[i]
                        changed = True

    return value, policy


# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0]) - 1]  # Goal is in top right corner
cost_step = 1
collision_cost = 100.
success_prob = 0.5

value, policy = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print row
for row in policy:
    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
