colors = [['red', 'green', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']

motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8


def show(p):
    for i in range(len(p)):
        print p[i]


# DO NOT USE IMPORT
# ENTER CODE BELOW HERE
# ANY CODE ABOVE WILL CAUSE
# HOMEWORK TO BE GRADED
# INCORRECT

p = []

colorRows = len(colors)
colorCols = len(colors[0])
colorNum = colorRows * colorCols

# Initialize p
for row in range(colorRows):
    newRow = []
    for col in range(colorCols):
        newRow.append(1. / colorNum)
    p.append(newRow)


def move(p, movement):
    right = movement[1]
    down = movement[0]
    if ((right != 0 and down != 0) or (right == 0 and down == 0)):
        # assumes that you can't go two directions at once, and to do nothing on [0,0]
        return p
    pNew = []
    if (right != 0):
        for row in range(colorRows):
            newRow = []
            for col in range(colorCols):
                m = p_move * p[row][(col - right) % colorCols]
                m += (1. - p_move) * p[row][col]
                # print m
                # print col
                newRow.append(m)
            pNew.append(newRow)
        return pNew

    if (down != 0):
        for row in range(colorRows):
            newRow = []
            for col in range(colorCols):
                m = p_move * p[(row - down) % colorRows][col]
                m += (1. - p_move) * p[row][col]
                newRow.append(m)
            pNew.append(newRow)
        # assumes that we can't
        return pNew


def sense(p, Z):
    q = []
    # Update step
    for row in range(colorRows):
        newRow = []
        for col in range(colorCols):
            hit = (Z == colors[row][col])
            newRow.append(p[row][col] * (hit * sensor_right + (1 - hit) * (1 - sensor_right)))
        q.append(newRow)

    # Normalize step
    s = sum(sum(x) for x in q)
    for row in range(colorRows):
        newRow = []
        for col in range(colorCols):
            q[row][col] = q[row][col] / s
    return q


for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])

# Your probability array must be printed
# with the following code.

show(p)
