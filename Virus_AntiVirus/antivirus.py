#!/usr/bin/python
import os
SIGNATURE = "SIMPLE PYTHON VIRUS"
infected = None
path = os.path.abspath("")
fname = ""

def search(path):
    filestocheck = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestocheck.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            filestocheck.append(path+"/"+fname)
    return filestocheck

def check(filestocheck):
	infected = False
	for fname in filestocheck:
		#print("here is the file" + fname)
		for line in open(fname):
			if SIGNATURE in line and fname[-12:] == "antivirus.py":
				#print("is antivirus.py : " + fname)
				break
			elif SIGNATURE in line:
				print(fname + "is infected!!!")
				infected = True
				break
			#print( line + " this is the sig: " + SIGNATURE)
		if infected == False:
			print (fname + " is clean")
		infected = False

file2check = search(os.path.abspath(""))
check(file2check)







