import  os
import shutil as file
"""

Add input for a startpoint 
Use error handling for if the path is invalid or an if statement 
For the endpoint create a Folder FOR , TEXT, ZIP files and MUSIC/VIDEOS 




"""

Files_Startpoint = (r'C:/Users/yeahm/OneDrive/Desktop/OrganizeThis/OrganizeThis/')
Files_Endpoint_TEXT = (r'C:/Users/yeahm/OneDrive/Desktop/Endpoint/TEXT/')
Files_Endpoint_Winrar = (r'C:/Users/yeahm/OneDrive/Desktop/Endpoint/WINRAR/')
jay = os.listdir(Files_Startpoint)



for i in jay:
    if i[-3:] == 'txt' or i[-3:] == 'rtf':
         text_FILES = Files_Startpoint + i 
         text_FILES_END = Files_Endpoint_TEXT + i
         file.move(text_FILES, text_FILES_END)
         print("Moved Text file")   
    if i[-3:] == 'rar' or i[-3:] == 'zip':
         text_FILES = Files_Startpoint + i 
         text_FILES_END = Files_Endpoint_Winrar + i
         file.move(text_FILES, text_FILES_END)
         print("Moved Win rar files")
         





