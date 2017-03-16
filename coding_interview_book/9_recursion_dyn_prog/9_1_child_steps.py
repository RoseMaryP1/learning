# A child is running up a staircase with n steps, and can hop either 1, 2, or 3 steps at a time.
# Implement a method to count how many possible ways that the child can run up the stairs.


def get_steps(n, step=0):
    if step > 0:
        n -= step

        if n == 0:
            return 1
        if n < 0:
            return 0
    counts = 0
    counts += get_steps(n, 1)
    counts += get_steps(n, 2)
    counts += get_steps(n, 3)

    return counts


# Test counts.
print(get_steps(4))
print(get_steps(2))
print(get_steps(1))
print(get_steps(0))
print(get_steps(-1))
