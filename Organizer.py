"""START HERE!
Currently this is a quick little project i wanted to do to challenge myself!
The final goal is to organize different file extensions like Exe's, text documents and other files.
This simple program take in a file location as a start point, also known as the location of the files you select to be moved.
The intended functionality just moves files declared as executables by the os.listdir function which detects some exe files but not all!
"""

import os 
import shutil
import time
import sys


# A function that takes in input and removes whitespace then returns our input values
def Input_Func():
    Files_SP = input(r"please enter a valid folder you would like the program to start the sorting process: (ex: C:\Users\BOBBY\OneDrive\Desktop\: ").strip()
    Files_EP = input('Please enter a valid folder you would like the program to place the sorted files: ').strip()
    return Files_SP, Files_EP
# A function to check if the file path given is valid, if so we continue the program! 
def CheckFileIsValid(Files_SP,Files_EP):

    
    if os.path.exists(Files_SP):
        print("Valid Start Path")

    else:
        print("Invalid Start Path")
        time.sleep(3)
        print("Closing Program due to invalid Start path")
        sys.exit()
    
    if os.path.exists(Files_EP):
        print("Valid End Point")
        
    else:
        print("Invalid End Path")
        time.sleep(3)
        print("Closing Program due to invalid End Path")
        sys.exit()

# A sorting function the checks the directory and list files and then moves them depending on the last 3 characters of the listed files. 
def Sort_Exe(Corrected_Files_SP, Corrected_Files_EP):

    ListOfFiles = os.listdir(Corrected_Files_SP) 
    print(ListOfFiles)

    
    for i in ListOfFiles:
        if i[-3:] == 'lnk'or i[-3:] == 'url' or i[-3:] == 'exe':
            src_file = os.path.join(Corrected_Files_SP, i)
            dst_file = os.path.join(Corrected_Files_EP, i)
            shutil.move(src_file, dst_file)


# A dial menu 
def menu_selection(Corrected_Files_SP, Corrected_Files_EP):
    print("Enter a valid operation by picking a number!")
    print("Enter 1 for sorting Exe's: ")
    Function_input = input("")
    if Function_input == '1':
        Sort_Exe(Corrected_Files_SP, Corrected_Files_EP)
    else:
        print("Invalid selection, ")

# A main function
def main():
    
    Files_SP,Files_EP = Input_Func()
    CheckFile = CheckFileIsValid(Files_SP,Files_EP)
    Corrected_Files_SP = r'' + Files_SP
    Corrected_Files_EP = r'' + Files_EP
    Menu = menu_selection(Corrected_Files_SP, Corrected_Files_EP)

# Gives prioty to the main function and won't run any other function enless listed in the main function. 
if __name__ == '__main__':
    main()