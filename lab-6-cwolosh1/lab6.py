# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    ### Your Code Here ###
    """ Given an integer of a number of donuts, this function returns a string of the form 'Number of donuts: <count>', where count is the input.

        args: count[int] - a number of donuts

        return: a string of the form 'Number of donuts: <count>', where count is the input and count = 'many' if count is 10 or more.
    """

    return "Number of donuts: " + str(count) if count < 10 else "Number of donuts: many"

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    ### Your Code Here ###
    """ Given a string s, this function returns a string made of the first 2 and last 2 characters of the original string, and returns an empty string if the original string is less than 2 characters.

        args: s[str] - any string of any length.

        return: a string that is the first two and last two characters of the original string, or an empty string.
    """

    return "" if len(s) < 2 else s[:2] + s[-2:]

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    ### Your Code Here ###
    """ Given a string s, this function returns a string where all occurences of its first character have been changed to '*', except for the first character itself.
        
        args: s[str] - any string of any length

        return: a string where all occurences of its first character have been changed to '*', except for the first character itself.
    """

    return s[0] + s.replace(s[0], "*")[1:]

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(prefix," got: ", got," expected: ", expected)


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

main()
