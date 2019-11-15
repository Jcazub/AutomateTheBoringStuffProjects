#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# TODO: Seperate lines and add stars
lines = text.split('\n')  # split the text for easier processing
for i in range(len(lines)):
    lines[i] = '*' + lines[i]  # add star to each string

text = '\n'.join(lines)  # join back into one string

pyperclip.copy(text)  # copy back to clipboard
