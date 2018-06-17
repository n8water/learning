def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    my_string = ""

    for i in range(len(phrases)):
        if len(my_string) < 0:
            my_string = phrases[i]
        else:
            my_string = my_string + "," + phrases[i]

    my_string = my_string + " " + phrases[i]
    new_string = my_string.replace('right', 'left')

    return(new_string)


if __name__ == '__main__':
    # These "asserts" using only for
    # self-checking and not necessary for
    # auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
