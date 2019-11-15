import re

phoneNumRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # parenthesis denotes the different groupings to split the matched results
# if you need to match actual parenthesis, you can escape them with a \

search_string = 'My number is 415-555-4242.'

mo1 = phoneNumRegex1.search(search_string)
print('Phone number found: ' + mo1.group())

mo2 = phoneNumRegex2.search(search_string)
print('The area code is {}'.format(mo2.group(1)))
print('The number is {}'.format(mo2.group(2)))
print('The whole number is {}'.format(mo2.group(0)))

area_code, main_number = mo2.groups()  # groups() returns a tuple of all groupings
