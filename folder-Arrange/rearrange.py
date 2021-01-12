import os.path
import shutil
from pathlib import *

checkDirectory = "/Users/kavinselvaraj/Downloads"

dirName = ["png", "jpeg", "zip", "dmg", "Text", "page", "number"]

dirPath = "/Users/kavinselvaraj/Downloads/dmgfiles"


def makeDirectory(folderName):
    os.mkdir('/Users/kavinselvaraj/Downloads/' + folderName)


try:
    for i in dirName:
        makeDirectory(i)
        print(i)
except FileExistsError:
    pass


def getFileExtension():
    global ext
    # listFile = (file for file in os.listdir(checkDirectory) if os.path.isfile(os.path.join(checkDirectory, file)))
    listFile = os.listdir(checkDirectory)
    # print(listFile)

    for file in listFile:
        if file.split(".")[:-1] in dirName:
            ext = file.split(".")[:1] + "." + file.split(".")[-1]
        else:
            ext = file.split(".")[-1]
            path = os.path.abspath(file)
            # print(path)
            # os.rename( )


getFileExtension()
