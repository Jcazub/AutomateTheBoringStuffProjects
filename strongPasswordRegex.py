import re

passwordRegex = re.compile(r'''
    ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$
''', re.VERBOSE)

testCases = ['password', 'PassWord1', 'passwords']

print([passwordRegex.search(word) is not None for word in testCases])


