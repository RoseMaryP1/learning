# Imagine you're debugging a search algorithm, and you want a convenient way to send queries that have weighted terms.
# For example, when searching for "pizza brooklyn" you might want to weigh "pizza" more heavily than "brooklyn".

# Say we want to just type queries with weights into the search box. e.g. "pizza 0.8 brooklyn 0.2".

# Write a function that takes a single string argument (the raw query) and parses it into a data structure with repeated
# (term, weight) pairs.
# 1. Return an ordered collection sorted by weight.
# 2. Weights are optional.  The original example "pizza brooklyn" is a valid input, and so is e.g. "pizza 5 brooklyn".
#    Where weights are missing, assume some default.

import math


class Term(object):
    def __init__(self, term, weight=0.0):
        self.term = term
        self.weight = weight

    def __repr__(self):
        return "(%s, %f)" % (self.term, self.weight)


def is_number(string):
    try:
        x = float(string)
        if not math.isnan(x):
            return True
    except ValueError:
        pass
    return False


def parse_query(input, default_weight=1.0):

    #TODO: test that input follows our assumptions
    # - string always starts with a term, not a weight.
    # - everything is simple ascii, not unicode.
    # - input is actually a string.
    # - assuming a single space as a split [ Update, allow for multiple spaces.]
    # - no multiple word terms.
    # - if negative weights are given, then that's what will be output. [Update, instead convert to default]
    # - weights to be sorted high to low.
    # - leading and trailing spaces are ignored.

    parts = input.split(" ") # assuming a single space as a split

    output =[]

    # Iterate over the parts
    found_word = None

    for part in parts:
        if found_word:
            if is_number(part):
                output.append(Term(found_word, float(part)))
                found_word = None
            else:
                output.append(Term(found_word, default_weight))
                found_word = part
        else:
            found_word = part

    # Cleanup found_word if there is one left.
    if found_word:
        output.append(Term(found_word, default_weight))

    output.sort(key=lambda x: x.weight, reverse=True)
    return output
# Tests

print(parse_query("dogs -5 cats 0"))
print(parse_query("dogs 5.0 cats 1.0"))
print(parse_query("dogs cats 12 bears"))
print(parse_query("cat      dog"))
print(parse_query("1.0 birds cats dogs 2 3 4")) # This assumes 1.0 is a search term, as well as "3"
print(parse_query("5birds cats1 d0gs")) # This will assume 1.0 is a search term.
print(parse_query(" birds cats1 d0gs ")) # This will assume 1.0 is a search term.






