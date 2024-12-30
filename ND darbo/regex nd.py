# 1.	Write a regex that validates if a string is a valid email address.  

# import re

# email = 'laura.185@gmail.com'

# # Regex for email validation
# IsEmail = re.compile(
#     r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# )

# if IsEmail.match(email):
#     print("Valid email address!")
# else:
#     print("Invalid email address!")



# 2.	Create a program that uses regex to extract all the dates from a given text.  


# import re

# def extractDates(text):
#     datePattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    
#     dates = datePattern.findall(text)
#     return dates

# print(extractDates('hello today is 01-12-2024'))



# 3.	Write a regex pattern that checks if a string is a valid phone number format (e.g., `(123) 456-7890`).  

# import re 
# def isValidNumber(number):
#     phonePattern = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}$')


#     if phonePattern.match(number):
#         print('valid')
#         return True
#     else: 
#         print('invalid')
#         return False


# isValidNumber('(123) 456-7890')
# isValidNumber('123 456-7890')



# 4.	Create a script that replaces all occurrences of a specific word in a text file using `re.sub()`.  


# import re

# def replaceWord(InputFile, outputFile, target, replacement):
#     try:
#         with open(InputFile, 'r') as file:
#             content = file.read()
        
#         pattern = re.compile(rf'\b{re.escape(target)}\b')

#         updatedText = pattern.sub(replacement, content)

#         with open(outputFile, 'w') as file:
#             file.write(updatedText)

#         print(f"All occurrences of '{target}' have been replaced with '{replacement}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# InputFile = 'file.txt'         
# outputFile = 'example_updated.txt' 
# target = 'Hello'            
# replacement = 'bye'        

# replaceWord(InputFile, outputFile, target, replacement)



