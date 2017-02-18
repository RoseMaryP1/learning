# Q: Given two strings, write a method to decide if one is a permutation of the other.


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    counts1 = count_chars(s1)
    counts2 = count_chars(s2)
    return compare_counts(counts1, counts2)


def count_chars(string):
    counts = dict()
    for c in string:
        if counts.get(c)is None:
            counts[c] = 0
        counts[c] += 1
    return counts


def compare_counts(c1, c2):
    if len(c1) != len(c2):
        return False
    chars = set(c1.keys()) | set(c2.keys())

    for c in chars:
        if c1.get(c) is None or c2.get(c) is None:
            return False
        if c1[c] != c2[c]:
            return False
    return True

if __name__ == '__main__':
    print(is_anagram("asdf", "afds"))
    print(is_anagram("asds", "afds"))




