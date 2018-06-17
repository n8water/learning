def checkio(text: str) -> str:
    output = {}
    letters = sorted(text.lower())
    # print(letters)
    for letter in letters:
        if letter.isalpha():
            if letter in output:
                output[letter] = output[letter] + 1
            else:
                output[letter] = 1

    result = max(output, key=output.get)

    return result

# print(checkio("Hello World!"))


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))


# These "asserts" using only for
# self-checking and not necessary for
# auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
