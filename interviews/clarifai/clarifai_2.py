# Suppose we have a frog named Bob who would like to go up a flight of N stairs.
#  Bob is peculiar in that he can only make leaps of size 1 or 2. Write a function
#  num_paths(N) which returns the number of possible ways Bob can go up the flight of stairs.

# We could solve it through brute force recursively, but would have exponential runtime, let's use dynamic
# programming instead. Also the number of times is going to explode exponentially so we might want to use bigint here.
def get_steps(n, cache={}):

    #TODO: test that cache is indeed a dict.

    if n < 0:
        return 0
    if n == 0:
        return 1
    if cache.get(n, None):
        return cache[n]
    cache[n] = get_steps(n - 1, cache) + \
               get_steps(n - 2, cache)
    return cache[n]


# Tests

#print(get_steps(1000)) 1000 fails due to maximum recursion depth.
print(get_steps(30))
print(get_steps(3))
print(get_steps(2))
print(get_steps(1))
print(get_steps(0))
print(get_steps(-1))


