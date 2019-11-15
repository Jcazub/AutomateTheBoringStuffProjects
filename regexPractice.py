import re

numDigit = re.compile(r'''
    ^\d{,3}(,\d{3})*$
    ''', re.VERBOSE)

#print(numDigit.search('12,456').group())

nameRegex = re.compile(r'''
    [A-Z]{1}[A-Za-z]+  # First Name
    \s  # space between first and last name
    Nakamoto
''', re.VERBOSE)

#print(nameRegex.search('rop Nakamoto').group())

sentenceRegex = re.compile(r'''
    (Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.
''', re.VERBOSE | re.IGNORECASE)

print(sentenceRegex.search('Carol eats cats').group())
