def palindrome(word):
    backward = word[::-1]
    if word==backward:
        same = 'y'
    else:
        same = 'n'
    return same
