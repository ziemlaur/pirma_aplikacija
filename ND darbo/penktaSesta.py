# What does the code for an empty dictionary look like?
    
# guests = {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
# dicte = {'foo': 42}

# 3. What is the main difference between a dictionary and a list?

# dictionary is unordered

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# KeyError: 'foo'

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# spam.keys explicitly checks if 'cat' is in the list of keys
# 'cat' in spam checks if cat is in spam dictionary and returns True or False value 


# 6. If a dictionary is stored in spam, what is the difference 
# between the expressions 'cat' in spam and 'cat' in spam.values()?

#cat' in spam checks if cat is in spam dictionary and returns True or False value 
#'cat' in spam.values() checks if there is cat in the values


# 7. What is a shortcut for the following code?

# if 'color' not in spam:
#     spam['color'] = 'black'

# spam.setdefault('color', 'black')

# 8. What module and function can be used to “pretty print” dictionary values?

# pprint module, 
# pprint.pprint()

# 1 What are escape characters?

# #\' \'' \t \n \\

# # 2. What do the \n and \t escape characters represent?

# # \n new line, \t tab

# # 3. How can you put a \ backslash character in a string?

# # raw string (r'')

# # 4. The string value ''Howl's Moving Castle" is a valid string. 
# # Why isn’t it a problem that the single quote character in
# # the word Howl's isn’t escaped?

# # double quote

# # 5. If you don’t want to put \n in your string, how can you write 
# # a string with newlines in it?

# # Multiline Strings with Triple Quotes

# # 6. What do the following expressions evaluate to?

# # 'Hello, world!'[1]
# # 'Hello, world!'[0:5]
# # 'Hello, world!'[:5]
# # 'Hello, world!'[3:]

# # e
# # Hello
# # Hello
# # lo, world!


# # 7. What do the following expressions evaluate to?

# # 'Hello'.upper()
# # 'Hello'.upper().isupper()
# # 'Hello'.upper().lower()

# #HELLO
# #True
# #hello


# # 8. What do the following expressions evaluate to?

# # 'Remember, remember, the fifth of November.'.split()
# # '-'.join('There can be only one.'.split())

# #['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
# # There-can-be-only-one.



# # 9. What string methods can you use to right-justify, 
# # left-justify, and center a string?

# rjust(), ljust() center()

# # # 10. How can you trim whitespace characters from the beginning 
# # or end of a string?

# strip(), rstrip(), and lstrip()



# inputas = input('ivesk teksta')
# vowels = "aeiouAEIOU"
# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# vowelsCount = 0
# consonantCount = 0

# for i in inputas:
#     if i in vowels:
#         vowelsCount += 1
#     elif i in consonants:
#         consonantCount += 1

# print(f"Vowels: {vowelsCount}, Consonants: {consonantCount}")

# grades = {"Laura": 80, "Marius": 78,"Lukas": 92,"Sandra": 88,"Evelina": 95}


# suma = sum(grades.values()) 
# skaicius = len(grades)            


# vidurkis = suma / skaicius

# print(f"Vidurkis: {vidurkis:.2f}")


# sakinys = "Pasibandymui testinis sakinys atsirado cia cia"

# zodziai = sakinys.split()


# zodziuCountas = {}

# for i in zodziai:
#     print(i)
#     if i in zodziuCountas:
#         zodziuCountas[i] += 1
#     else:
#         zodziuCountas[i] = 1

# for i, count in zodziuCountas.items():
#     print(f"{i}: {count}")


# loginas = {"user1": "password123","user2": "securepassword","user3": "mypassword"}

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username in loginas and loginas[username] == password:
#     print("Login successful!")
# else:
#     print("Invalid username or password.")
