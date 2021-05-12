# Reading Files: 
file = open("my_file.txt")  # To open the file.
contents = file.read()  # To read the file.
print(contents)
file.close()  # To close the file Manually. We had to close the file whenever we open it
# OR
with open("my_file.txt") as file:  # To open the file.
    contents = file.read()  # To read the file.
    print(contents)

# Writing to Files: 
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")  # To write in file.
    # mode is in by default 'r'(read) mode.
    # We had to change it to 'w'(write) to write.
    # But it deletes all the previous data.
    # Or we can use 'a'(append) to append new data.

# Opening a File that doesn't exit in write mode will create it from scratch:
# In write mode if we enter a file name that doesn't exist,
# Then it creates a new of that name.
# It only works when we are in the write mode and the file doesn't exist.
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
# For Example:
# Opening a File that doesn't exit in write mode will create it from scratch:
# with open("file_that_doesnt_exist.txt", mode="w") as file:
#     file.write("New text.")

# Modes:
# mode "r" is used to read the file.
# mode "w" is used to write in file.
# mode "a" is used to append in file.

# File Paths: 
# "/" Represent Root folder(C:/)

# File Paths:                          # Absolute File Path            # Relative File Path
#                                                                                                                                       
# /   Root                               /                               |
# |   (In Windows: C:/  |  In Mac: Macintosh HD)
# |__ Work (Folder)                      /Work                           |
#      |
#      |__ report.doc                    /Work/report.doc                ../report.doc  # If we are on Project Folder and we want to access file outside the folder.
#      |                                                                   (The .. goes up one folder)                       (or file outside the Working Directory)
#      |__ Project (Folder)              /Work/Project                   |
#            |
#            |__ talk.ppt                /Work/Project/talk.ppt          ./talk.ppt  # If file is in Working Directory. (If Project Folder is Working Direcitory)
#                                                                                    (If we are currently working in Project Folder)
#                                                                        ./Project/talk.ppt  # If Work Folder is working directory.
# 

# Relative File Path:

# /   Root   
# |
# |__ Work (Folder)                # We are working in Work Folder(Working Directory).
#      |
#      |__ report.doc              ./report.doc  or  report.doc  # To access report.doc file
#      |                                           ("./" is optional)
#      |__ main.py                 # We are on main.py
# 

# If we move the file from Working directory to Desktop.
# For accessing that file.
# Location of File: C:\Users\Aniruddh Upadhyay\Desktop
# Using Absolute File Path.
with open("/Users/Aniruddh Upadhyay/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Using Relative File Path.
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Absolute File Path: Absolute File Path is always relative to the root of the computer.
# (on Windows usually C-Drive until we change it and on Mac it is Macintosh HD)

# Relative File Path: The Relative File Path is relative to currently Working Directory.
# (so it depends on where we are and where we are trying to get to)
