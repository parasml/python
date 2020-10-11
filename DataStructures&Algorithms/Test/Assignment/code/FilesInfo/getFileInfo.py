#-----------------------------------------------------------
# To get file info in python
#-----------------------------
import os
import shutil


def getFileInfo():
    lsDirectory = os.listdir("C:\Prashan\DataLake")

    print("lsDirectory = ", lsDirectory)


def ZipFile():
    import shutil

    dir_name = "C:/Prashan/DataLake"
    output_filename = 'C:/Prashan/test'
    shutil.make_archive(output_filename, 'zip', dir_name)

def copyFileToOtherLocation():

    source = 'C:/Prashan/test.zip'
    destination = 'C:/Prashan/delete1/test.zip'
    dest = shutil.copyfile(source, destination) 

def unzipFile():
    '''
    import zipfile
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    '''

    filename = 'C:/Prashan/test.zip'
    extract_dir = 'C:/Prashan/delete1/'
    shutil.unpack_archive(filename, extract_dir)    

#-----------------------------------------------
# Function Calls
#-----------------
#getFileInfo()
#ZipFile()
#unzipFile()
copyFileToOtherLocation()
