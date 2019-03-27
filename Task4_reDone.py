import tkinter as tk
from tkinter import filedialog
import sys
import argparse
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    return parser
def fromfile():
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        f = open(file_path)
        str = f.readline()
        return str
    except IOError:
        print('Проблема с файлом')
def fromConsole():
    return input()
"""def ChooseNumbers(str):
    mylist = list()
    line = ""
    i = 0
    while i < len(str):
        if str[i].isdigit():
            j = i
            while (str[j].isdigit() or (str[j] == '.' and line.find('.') == -1 and line.find(',') == -1) or (
                    str[j] == ',' and line.find(',') == -1 and line.find('.') == -1)) and j < len(str):
                line += str[j]
                j += 1
                if(j >= len(str)):
                    mylist.append(line)
                    return mylist
            if line[len(line)-1] == '.' or line[len(line)-1] == ',':
                line = line[:-1]
            mylist.append(line)
            i = j
            line = ""
        else:
            i += 1
    return mylist"""

def ChooseNumbers(str):
    mylist = list()
    line = ""
    i = 0
    while i < len(str):
        if str[i].isdigit():
            while i < len(str) and str[i].isdigit():
                line += str[i]
                i += 1
            if i < len(str) and ((str[i] == '.' and line.find('.') == -1 and line.find(',') == -1) or \
                    (str[i]==',' and line.find(',') == -1 and line.find('.') == -1)):
                if i < len(str)-1:
                    if str[i+1].isdigit():
                        line+=str[i]
                i+=1
            while i < len(str) and str[i].isdigit():
                line += str[i]
                i+=1
        else:
            i+=1
            #
        if line!="":
            mylist.append(line)
        line = ""
    return mylist
if __name__=='__main__':
    parser = createParser()
    namespace = parser.parse_args()
    if namespace.command == 'f':
        mylist = fromfile()
    if namespace.command == 'c':
        mylist = fromConsole()
    resultlist = ChooseNumbers(mylist)
    for i in resultlist:
        print(i)