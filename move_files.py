import os
import shutil

source= "C:/Users/ACER/Downloads"
dest = "C:/Users/ACER/Desktop/document_files"

list_of_files=os.listdir(source)

for file_name in list_of_files:
    root,ext = os.path.splitext(file_name)
    if ext=='':
        continue
    else:
        if ext in  [ '.txt', '.doc', '.docx', '.pdf']:
            path1=source + "/"+file_name
            path2=dest+"/"+"document_files"
            path3=dest+"/"+"document_files"+file_name

            if os.path.exists(path2):
                print("moving..................",file_name)
                shutil.move(path1,path3)

            else:
                os.mkdir(path2)
                print("moving...............",file_name)
                shutil.move(path1,path3)