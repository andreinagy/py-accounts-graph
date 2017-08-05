# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "File Finder"

import os

def cwd():
    cwd = os.getcwd()
    return(cwd)
    
    
def findFilesInDirectory (baseDirectory, extension) :
    files = []
    for r,d,f in os.walk(baseDirectory):
        for file in f:
            if file.endswith(extension):
                fileWithPath = os.path.join(r,file)
                files.append(fileWithPath)
    return files