#!C:\Python27\python.exe

## Metin2 Patch Creator v1.1 (By Arves100)
## Version 1.1:
###			Semplified Module Loading
## Version 1.0:
###			Initial Build

## Windows Notes: Install Diff command from GnuWin32 or MinGW

## Sample Usage:
##		PatchCreator.Create(Directory name,File name)

import os

def Create(dir,file):
	if dir == None:
		raise(Exception, "Cannot read a Null Directory!")
	if not os.path.isdir("patch/" + dir):
		os.makedirs("patch/" + dir)
	os.system("diff -Naur old/" + dir + "/" + file.replace("\n","") + " new/" + dir + "/" + file.replace("\n","") + " > patch/" + dir + "/" + file.replace("\n","") + ".diff")
	print("Creating Patch: " + dir + "/" + file.replace("\n","") + " ...")

def BuildFromList(file):
	a = open(file,"r")
	for line in a:
		b = line.replace("\n","")
		for line in open("list/" + b + ".list","r"):
			Create(b,line)
	a.close()