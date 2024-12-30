# # 1. What is the function that creates Regex objects?

# re.compile()

# # 2. Why are raw strings often used when creating Regex objects?

# Raw strings (prefix r) treat backslashes (\) as literal characters, avoiding the need to escape them.

# # 3. What does the search() method return?

# Match object

# # 4. How do you get the actual strings that match the pattern from a Match object?

# group()

# # 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

# Group 0: The entire match (e.g., 123-456-7890).
# Group 1: The first set of parentheses (e.g., 123).
# Group 2: The second set of parentheses (e.g., 456-7890).

# # 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

#  (, \), and \.


# # 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
# If the regex has no capturing groups, findall() returns a list of strings.
# If the regex has capturing groups, findall() returns a list of tuples (one tuple for each match, containing the groups).


# # 8. What does the | character signify in regular expressions?
# either meaning 

# # 9. What two things does the ? character signify in regular expressions?
# Optional match, non greedy.

# # 10. What is the difference between the + and * characters in regular expressions?
# + 1 or more 
# * 0 or more

# # 11. What is the difference between {3} and {3,5} in regular expressions?

# {3}: Matches exactly 3 occurrences 
# {3,5}: Matches between 3 and 5 occurrences 

# # 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

# \d: Matches any digit (0-9).
# \w: Matches any alphanumeric character (a-z, A-Z, 0-9, _).
# \s: Matches any whitespace character (spaces, tabs, newlines).

# # 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

# \D: Matches any non-digit.
# \W: Matches any non-alphanumeric character.
# \S: Matches any non-whitespace character.

# # 14. What is the difference between .* and .*??

# .*: Matches as many characters as possible (greedy).
# .*?: Matches as few characters as possible (non-greedy).

# # 15. What is the character class syntax to match all numbers and lowercase letters?

# [0-9a-z]

# # 16. How do you make a regular expression case-insensitive?

# re.IGNORECASE (or re.I)  to re.compile().

# # 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

#  . matches any character except newline.
# With re.DOTALL, it matches any character, including newlines.

# # 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

# 'X drummers, X pipers, five rings, X hens'

# # 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

# It allows you to write regex patterns with whitespace and comments, improving readability.

# # 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

# # '42'
# # '1,234'
# # '6,368,745'
# # but not the following:
# # '12,34,567' (which has only two digits between the commas)
# # '1234' (which lacks commas)

# r'^\d{1,3}(,\d{3})*$'

# # 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

# # 'Haruto Watanabe'
# # 'Alice Watanabe'
# # 'RoboCop Watanabe'
# # but not the following:
# # 'haruto Watanabe' (where the first name is not capitalized)
# # 'Mr. Watanabe' (where the preceding word has a nonletter character)
# # 'Watanabe' (which has no first name)
# # 'Haruto watanabe' (where Watanabe is not capitalized)

# r'^[A-Z][a-z]*\sWatanabe$'

# # 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

# # 'Alice eats apples.'
# # 'Bob pets cats.'
# # 'Carol throws baseballs.'
# # 'Alice throws Apples.'
# # 'BOB EATS CATS.'
# # but not the following:
# # 'RoboCop eats apples.'
# # 'ALICE THROWS FOOTBALLS.'
# # 'Carol eats 7 cats.'

# r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$'