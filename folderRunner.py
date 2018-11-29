
import os

base = "\\\hawkeye\\archive\\"
yearFolder = '2017\\'
job = '15083'

combined = base+yearFolder
slash = '\\'

def hasSuffix(path):
    """ Check to see if job has suffixes attached.
    
    Args:
        path(str)
    Returns: bool    
    """

    for dirs in os.listdir(path):
        if(os.path.isdir(path+slash+dirs)):
            if(dirs.startswith('_')):
                print('Yeah Suffix')
            else:
                False




def isOld(path):
    """ Check to see if folder is of the old type.
    
    Args:
        path (str)
    
    Returns:bool
        """
    for dirs in os.listdir(path):
        # print('Looking at ',dirs)
        
        
        # print(path+slash+dirs)
        if(os.path.isdir(path+slash+dirs)):
            # print('Inside isdir',dirs)
            if(dirs.startswith('0')):
                print("False, ie it is new", dirs)
                return False
            else:
                return True    


        # if(dirs.startswith('0')):
        #     print("False, ie it is new", dirs)
        #     return False
        # elif(dirs.startswith("_")):
        #     print("this has a suffix")
        # #     findParents(path)   

    

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
            
        #print(jobNumber)
        #show Contents
        # for data in os.listdir(path+jobNumber):
        #     fullpath = path+jobNumber+'\\'+data
        #     print(fullpath)
            
        
#folder(combined+"09020")
isOld(combined+"17208")
hasSuffix(combined+"17208")
isOld(combined+"17209")
hasSuffix(combined+"17209")
#findParents(combined)
#print(combined)


