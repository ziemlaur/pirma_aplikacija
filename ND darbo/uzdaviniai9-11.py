from pathlib import Path
# 1.	Write a program that reads a text file and prints out each line with line numbers.  
# from pathlib import Path

# kelias = Path('D:\\PYTON\\pirma_aplikacija\\file.txt')
# with kelias.open() as file:
#     content = file.readlines()

# for line_number, line in enumerate(content, start=1):
#     print(f"{line_number}: {line.strip()}")

# 2.	Create a program that writes user input to a text file and saves it for future use.  



# file_path = Path('file.txt')


# user_input = input("Enter your input:")
# with file_path.open('a') as file:  

#     file.write(user_input + '\n')  



# 3.	Write a program that handles file not found errors when trying to open a file.  

# file_name = input("Enter the name of the text file to open: ")

# file_path = Path(file_name)

# try:
#     with file_path.open('r') as file:
#         content = file.readlines()
#         print("\nFile content:")
#         for line in content:
#             print(line.strip())  
#             break  

# except FileNotFoundError:
#     print(f"Error: The file '{file_name}' was not found.")


# 4.	Create a program that reads a file and counts the number of words.  


# kelias = Path('D:\\PYTON\\pirma_aplikacija\\file.txt')

# zodziai = 0

# with kelias.open() as file:
#     content = file.readlines()  

# for line in content:
#     words = line.split()  
#     zodziai += len(words)  

# print(f"The total number of words in the file is: {zodziai}")

# 5.	Write a program that creates a new folder and copies all `.txt` files into it.  
# import os
# import shutil
# from pathlib import Path

# source_dir = Path('D:\\PYTON\\pirma_aplikacija')
# new_folder_name = 'txt_files'

# new_folder_path = source_dir / new_folder_name

# new_folder_path.mkdir()

# for file in source_dir.glob('*.txt'):
#     shutil.copy(file, new_folder_path) 

# print(f"All .txt files have been copied to: {new_folder_path}")

# 6.	Create a script that renames all files in a directory to include today's date in their filenames.  

# import os
# from datetime import datetime
# from pathlib import Path

# directory = Path('D:\\PYTON\\pirma_aplikacija')

# today_date = datetime.now().strftime('%Y-%m-%d')

# for file in directory.iterdir():
#     if file.is_file():  
 
#         new_filename = f"{today_date}_{file.name}"
#         new_file_path = file.parent / new_filename  

  
#         file.rename(new_file_path)
#         print(f"Renamed '{file.name}' to '{new_filename}'")

# print("All files have been renamed to include today's date.")


# 7.	Write a program that checks if a specific file exists in a directory and prints its size.  
# from pathlib import Path


# directory = Path('D:\\PYTON\\pirma_aplikacija')
# file_name = 'file.txt'  

# file_path = directory / file_name


# if file_path.exists() and file_path.is_file():
#     file_size = file_path.stat().st_size  
#     print(f"The file '{file_name}' exists and its size is {file_size} bytes.")
# else:
#     print(f"The file '{file_name}' does not exist in the specified directory.")


# 8.	Create a program that backs up a folder by copying its contents to another location. 
# import shutil
# from pathlib import Path


# source_dir = Path('D:\\PYTON\\pirma_aplikacija')  
# backup_dir = Path('D:\\PYTON\\pirma_aplikacija_backup') 


# backup_dir.mkdir()

# try:
#     for item in source_dir.iterdir():  
#         if item.is_file():
#             shutil.copy(item, backup_dir)  
#             print(f"Copied file: {item.name} to {backup_dir}")

#         elif item.is_dir():
#             shutil.copytree(item, backup_dir / item.name) 
#             print(f"Copied directory: {item.name} to {backup_dir}")
             
# except Exception as e:
#     print(f"An error occurred: {e}")

# print(f"Backup completed. All contents from {source_dir} have been copied to {backup_dir}.")

# #  

