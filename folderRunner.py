
import os

base = "\\\hawkeye\\archive\\"
yearFolder = '2015\\'
job = '15083'

combined = base+yearFolder+job

""" Check to see if folder is of the old type """
def isOld(path):
    for dirs in os.listdir(path):
        print(dirs)
        if(dirs.startswith('0')):
           return print("This is new Style")




isOld(combined)
print(combined)

