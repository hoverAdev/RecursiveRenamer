import sys
import os

def main(pref, path):
    if((type(pref) != type("")) or (type(path) != type(""))):
        print("Invalid arguments, need strings")
        return(1)
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

def parser(args):
    match len(args):
        case 0:
            print("No app name detected")
            return(1)
        case 1:
            print("Invalid number of arguments")
            print("usage: " + args[0] + " <prefix> [directory]")
            print()
            return(1)
        case 2:
            main(args[1], os.getcwd())
        case _:
            main(args[1], args[2])

parser(sys.argv)

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