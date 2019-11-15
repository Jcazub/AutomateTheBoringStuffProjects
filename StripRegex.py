import re


def strip_using_regex(word, strip=' '):
    strip_regex = re.compile(strip + '*')
    word = strip_regex.sub('', word)
    return word


print(strip_using_regex('abHicab', 'v'))
