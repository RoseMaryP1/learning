# coding=utf-8
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional
# data structures?
import array


# Determine if a character has unique characters (Simple answer using python set())
def has_unique_chars(test_string):
    found = set()
    for char in test_string:
        if char in found:
            return False
        else:
            found.add(char)
    return True


# If we were doing this only with python arrays.
def has_unique_chars_alt(test_string):
    """Verify that a character array has unique strings.

    Args:
        test_string (str): The String to test.
    Return: Boolean
    """
    test_string_u = unicode(test_string, encoding='utf-8')
    found = array.array("u")

    for char in test_string_u:
        # Check if it's found.
        # Binary search is probably overkill, especially for UTF-8, but why not?
        if contains_char(found, char):
            return False
        else:
            # Add it and resort the list.
            ordered_add(found, char)
            pass
    return True


def contains_char(search, char):
    """Check an ordered list of characters to see if one exists.
    Args:
        search (array.array): The String to test.
        char(Char): The character to find.
    Return: Boolean
    """
    if type(search) != array.array:
        raise TypeError("search should be 'array.array' but is %s" % (type(search)))
    if type(char) != unicode:
        raise TypeError("arr should be 'unicode' but is %s" % (type(char)))
    first = 0  # type: int
    last = len(search) - 1  # type: int
    found = False  # type: bool

    while first <= last and not found:
        mid = (first + last) // 2

        if search[mid] == char:
            found = True
        else:
            if char > search[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found


# Let's also review sorting.
def ordered_add(arr, char):
    """Add an item to an already sorted array
    Args:
        arr (array.array): The array to add the char to.
        char (unicode): The character to be added.
    """
    # If the array is empty, just add the item.
    # Otherwise find the item between the next smaller and next larger.
    # [a, c, d, z] and add an 'e'
    first = 0
    last = len(arr) - 1
    found = False

    if type(arr) != array.array:
        raise TypeError("arr should be 'array.array' but is %s" % (type(arr)))
    if type(char) != unicode:
        raise TypeError("arr should be 'unicode' but is %s" % (type(char)))

    while first <= last and not found:
        split = (first + last) // 2
        if arr[split] == char:
            found = True
        else:
            if char > arr[split]:
                first = split + 1
            else:
                last = split - 1
    if not found:
        # insert will add
        arr.insert(first, char)

# Tests
str_a = "This is a string with duplicates"
str_b = "nodupes"
# Note: we need to add coding=utf-8 to the top of the page to support Python 2.
str_c = "Unicode: ←"
str_empty = ""

if __name__ == '__main__':
    print(has_unique_chars(str_empty))
    print(has_unique_chars(str_a))
    print(has_unique_chars(str_b))
    print(has_unique_chars(str_c))
    print(has_unique_chars_alt(str_empty))
    print(has_unique_chars_alt(str_a))
    print(has_unique_chars_alt(str_b))
    print(has_unique_chars_alt(str_c))
