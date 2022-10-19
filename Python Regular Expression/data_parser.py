"""
Import all the phone numbers from the given text file.
[ Different types of scenarios are built inside the "simple.py" file ]
"""

import re

# Scenario: Build a pattern to extract all the data from the "data.txt" file.
pattern = re.compile('\d\d\d.\d\d\d.\d\d\d\d')

phone_nums = []

with open('Python Regular Expression\data.txt', 'r') as f:
    contents = f.readlines()    # break every content into newline, put into a list as elem
    # print(contents)
    for line in contents:
        # print(line, end='')
        matches = pattern.finditer(line)    # implement regex-pattern in each list-elem (each line)
        for mtch in matches:
            # print(mtch.group()) # extract the matche-attr-value from the matched-object
            phone_nums.append(mtch.group())     # [ Inspired from ]: https://stackoverflow.com/a/15340666

# print(len(phone_nums))

for num in phone_nums:
    print(num)
