# checkio
# Home Insel
# House Password

# Vorgaben:
# The password will be considered strong enough if its length is greater than
# or equal to 10 symbols, it has at least one digit, as well as containing one
# uppercase letter and one lowercase letter in it. The password contains only
# ASCII latin letters or digits.

#Input: A password as a string.
#Output: Is the password safe or not as a boolean or any data type that can
# be converted and processed as a boolean. In the results you will see the
# converted results.

def checkio(data):
    #Bedingungen überprüfen

    length = False
    lower = False
    upper = False
    digit = False

    safe = False

    if len(data) >= 10:
        length = True
        #print(length)

    for c in data:
        if c.islower():
            lower = True
        elif c.isupper():
            upper = True
        elif c.isdigit():
            digit = True
        else:
            return False

    safe = length and lower and upper and digit
    return safe

#print (checkio('QWERTYqwerty'))
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
