import sys
import os

def main(pref, path):
    pref = str(pref)
    path = str(path)
    
    if(not os.path.exists(path)):
        print("Invalid path")
        return(1)
    
    inpt = os.listdir(path)
    
    for file in inpt:
        file = os.path.realpath(path + "/" + file)
        
        if not os.access(file, os.W_OK):
            print("Cannot access file " + file)
        else:
            fldr = os.path.dirname(file) + "/"
            
            flnm = os.path.basename(file)
            flnm = flnm.replace(pref, "")
            flnm = flnm.strip()
            
            os.replace(file, fldr + flnm)
            
    return(0)

def parser(args):
    if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 10):
        print("Please use Python 3.10 or higher.")
        return(1)
    match len(args):
        case 0:
            print("No app name detected")
            return(1)
        case 1:
            print("usage: " + args[0] + " <prefix> [directory]")
            print()
            return(0)
        case 2:
            errcode = main(args[1], os.getcwd())
            return(errcode)
        case _:
            errcode = main(args[1], args[2])
            return(errcode)

errcode = parser(sys.argv)

print("Program exited with code " + str(errcode))
sys.exit(errcode)

"""
RecursiveRenamer.py
Ambience Town 2024

args: array of arguments
pref: prefix to remove
path: path to directory with files to rename
inpt: input files from directory "path"
file: file being manipualated
fldr: "file dir", directory of file being manipulated
flnm: "file name", name of file being changed
"""