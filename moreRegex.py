import re

def returnIfNotNone(object):
    if object is not None:
        return object
    else:
        return "WRONG ANSWER!!!"

batRegex = re.compile(r'(Bat(wo)*man)')
mo = batRegex.search("The Adventures of Batwowoman")

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

print(returnIfNotNone(phoneRegex.search('(718.530.3899')))
print(mo.group(1))

