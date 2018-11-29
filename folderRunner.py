
import os

base = "\\\hawkeye\\archive\\"
yearFolder = '2017\\'
job = '15083'

combined = base+yearFolder

def isOld(path):
    """ Check to see if folder is of the old type.
    
    Args:
        path (str)
    
    Returns:
        bool"""
    for dirs in os.listdir(path):
        print('Looking at ',dirs)

        if(dirs.startswith('0')):
            print("False, ie it is new")
            return False
        elif(dirs.startswith("_")):
            print("this has a suffix")
        #     findParents(path)   

    

def findParents(path):
    """ Find Parent folders
    
    Args:
        path (str)
    
    Returns:
        dunno yet"""
    for jobNumber in os.listdir(path): #get job number and enter
        jobNumber = str(jobNumber)
        #print(path+jobNumber)
        isOld(path+jobNumber)
        if isOld == False:
            print(jobNumber, "Is New style")
            m = jobNumber
        elif isOld == True:
            print(jobNumber + " Is is old school")
        else: 
            print("Unidentified")        
        #print(jobNumber)
        #show Contents
        # for data in os.listdir(path+jobNumber):
        #     fullpath = path+jobNumber+'\\'+data
        #     print(fullpath)
            
        

isOld(combined+"17208")
#findParents(combined)
#print(combined)


