# This mission is the first one of the series. Here you should find the
# length of the longest substring that consists of the same letter.
# For example, line "aaabbcaaaa" contains four substrings with the same letters
# "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes
# it an answer.
# Input: String.
# Output: Int.

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    count = 0
    counts = []
    letter = ""
    for c in line:
        if c == letter:
            count +=1
        else:
            counts.append(count)
            letter = c
            count = 1
    counts.append(count)
    if len(counts) == 0:
        return 0

    return max(counts)

print(long_repeat('ffff'))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert long_repeat('sdsffffse') == 4, "First"
#     assert long_repeat('ddvvrwwwrggg') == 3, "Second"
#     assert long_repeat('abababaab') == 2, "Third"
#     assert long_repeat('') == 0, "Empty"
#     print('"Run" is good. How is "Check"?')
