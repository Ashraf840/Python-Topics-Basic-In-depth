import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Has HasHas

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
879-145-7457
321.--555.--4321
123.555.1234
123*555*1234
800@555@1234
800#555#1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
pat
mat
bat

'''

# print(r"\tTab")  # Regular expression will interpret the string before Python doing anything
# Create pattern, case-sensitive; follows alphabet order strictly
# pattern = re.compile(r'.')  # Allows to separate the patterns into variables; reuse the variables to multiple searches

# Scenario: Match email
# pattern = re.compile(r'coreyms.com')    # [ Works OK ]
# pattern = re.compile(r'coreyms\.com')   # escape the backslash-dot

# Scenario: Pattern to find any (single) digit from 0-9
# pattern = re.compile(r'\d')

# Scenario: Pattern to find anything which is not a digit from 0-9; includes special characters, whitespaces, tabs, newlines
# pattern = re.compile(r'\D')

# Scenario: Pattern to find a word character (a-z, A-Z, 0-9); ignore the special characters
# pattern = re.compile(r'\w')

# Scenario: Pattern to find any whitespace, tab, newline
# pattern = re.compile(r'\s')

# Scenario: Pattern to find not whitespace, tab, newline. 
# Includes alphabets with the special characters . ^ $ * + ? { } [ ] \ | ( )
# pattern = re.compile(r'\S')

# # Scenario: Pattern to find the "Has" which has word-boundaries after
# pattern = re.compile(r'Has\b')

# Scenario: Pattern to find the "Has" which doesn't have word-boundaries after
# pattern = re.compile(r'Has\B')

# Use the pattern that matches literal characters into the string
# matches = pattern.finditer(text_to_search)

sentence = 'Start a sentence and then bring it to an end'

# # Caret (^) matches the beginning of the string
# pattern = re.compile(r'^Start')
# matches = pattern.finditer(sentence)

# # Dollar ($) matches the end of the string
# pattern = re.compile(r'an$')
# matches = pattern.finditer(sentence)



# # Scenario: Pattern to find the phone nums within the multiline string.
# # To match the first 3 digits of the phone nums use the "\d\d\d".
# # To match the dot(.) or hyphen(-) in between, use dot(.) in the pattern.
# # To match the middle 3 digits, again use the "\d\d\d". Use dot(.) to match whether the dot/hyphen.
# # Then the last 4 digits will be matched using "\d\d\d\d".
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # matches any char in the phone-numbers

# Use character-set (brackets) to define which chars to be considered
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # matches only the dot(.) or hypen(-) chars in the phone-numbers
# pattern = re.compile(r'\d\d\d[-.#]\d\d\d[-.#]\d\d\d\d') # matches only the dot(.) or hypen(-) or hash(#) chars in the phone-numbers
# pattern = re.compile(r'\d\d\d[-.#]+\d\d\d[-.#]+\d\d\d\d') # matches only the dot(.) or hypen(-) or hash(#) chars in the phone-numbers. One or more of the multiple choices

# Matches the nums 
# pattern = re.compile(r'[89]00-\d\d\d-\d\d\d\d')       # Matches only 800 or 900 as the first 3 digits from the numbers with hyphen(-) only
# pattern = re.compile(r'[89]\d\d-\d\d\d-\d\d\d\d')     # matches nums starts with 8 or 9 with the defined pattern

# Scenario: Matches only the characters (nums) form 1 to 5 the string.
# pattern = re.compile(r'[1-5]')

# Scenario: Matches only the characters (lower-case alphabets) form a to z the string.
# pattern = re.compile(r'[a-z]')

# Scenario: Matches only the characters (both lower-case & upper-case alphabets) form aA to zZ the string.
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[a-z-A-Z]')  # includes lower & upper case alphabets, also the hyphens (-).

# Scenario: Matches only the characters which are not form aA to zZ the string using caret (^) in a characterset.
# pattern = re.compile(r'[^a-zA-Z]')

# Scenario: Matches the characters which are not starting with 'b' followed by 'at' from the string using caret (^) in a characterset.
# pattern = re.compile(r'[^b]at')

# # Scenario: Matches the phone numbers using quantifiers
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')


# Scenario: Matches the person-names with the prefixes "Mr"
# pattern = re.compile(r'Mr\.')   # to match the non-unicode-chars dot(.) as suffix of "Mr"
# pattern = re.compile(r'Mr\.?')   # to match both the non-unicode-chars dot(.) or not-dot as suffix of "Mr". 0 or 1 chars by the "?"
# pattern = re.compile(r'Mr\.?\s')   # inlcudes matching a whitespace after by "\s" matches only the "Mr./Mr "
# pattern = re.compile(r'Mr\.?\s[A-Z]') # inlcudes the uppercase letter of the firstname
# pattern = re.compile(r'Mr\.?\s[A-Z]\w')  # includes one more letter after the uppercase chars in the firstname
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')  # includes the rest of the chars in the firstname; doesn't match the "Mr. T", since this pattern expects one or more chars after the uppercase
# pattern = re.compile(r'Mr\.?\s[A-Z]?\w+')  # includes the rest of the chars in the firstname; matches "Mr. T", since the pattern expects whether only an uppercase char or an uppercase char followed by other chars
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  # includes 0 or more chars after the uppercase letter of the firstname

# TIMESTAMP: 00:31:00


# Use the pattern that matches literal characters into the string
matches = pattern.finditer(text_to_search)



count = 0

for match in matches:
    print(match)
    count += 1
    # print(match.span())
    # print(text_to_search[match.span()[0]:match.span()[1]])

print("Total matches: ", count)