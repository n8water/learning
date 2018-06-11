# This mission is the part of the set. Another one - Caesar cipher decriptor.
#
# Your mission is to encrypt a secret message (text only, without special chars
# like "!", "&", "?" etc.) using Caesar cipher where each letter of input text
# is replaced by another that stands at a fixed distance.
# For example ("a b c", 3) == "d e f"
# Input: A secret message as a string (lowercase letters only and white spaces)
# Output: The same string, but encrypted

def to_encrypt(text, delta):
    """Function to alter the input text by delta positions"""
    output = ""
    for c in text:
        if c.islower():
            new = ord(c) + delta
            if new > 122:
                new = new - 26
                output += chr(new)
            elif new < 97:
                new = new + 26
                output += chr(new)
            else:
                output += chr(new)
        else:
            output += c

    return output


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
