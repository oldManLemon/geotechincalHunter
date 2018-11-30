
import os

base = "\\\hawkeye\\archive\\"
yearFolder = '2010\\'
job = '15083'

combined = base+yearFolder
slash = '\\'


def hasSuffix(path):
    """ Check to see if job has suffixes attached.

    Args:
        path(str)
    Returns: Returns a list of Suffixes or False   
    """
    suffixList = []
    for dirs in os.listdir(path):
        if(os.path.isdir(path+slash+dirs)):

            if(dirs.startswith('_')):

                # print('Yeah Suffix')
                suffixList.append(dirs)
                # print(suffixList)

                # return True
    if(len(suffixList) > 0):
        print(suffixList)
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


def oldStyleHunterGeo(path, searchTerm):
    """ Old style folder scanner and hunter
    Args:
        File path (str)
        Searchable Object (str)

    Returns: 
        Returns an array

     """
    location = []
    for dirs in os.listdir(path):
        if(dirs.startswith('doc')): #Limits search directory. Also ignores Suffixes
            for dirPath, walkDirs, files in os.walk(path+slash+dirs):
                for line in walkDirs:
                    if searchTerm.lower() in line.lower():
                        #print("Found", dirPath+slash+line)
                        location.append(dirPath+slash+line)
                for line in files:
                    if searchTerm.lower() in line.lower():
                        #print("Found", dirPath+slash+line)
                        location.append(dirPath+slash+line)
    return(location)           
              
                


def findParents(path):
    """ Find Parent folders

    Args:
        path (str)

    Returns:
        dunno yet"""
    for jobNumber in os.listdir(path):  # get job number and enter
        jobNumber = str(jobNumber)
        # print(path+jobNumber)
        isOld(path+jobNumber)

        # print(jobNumber)
        # show Contents
        # for data in os.listdir(path+jobNumber):
        #     fullpath = path+jobNumber+'\\'+data
        #     print(fullpath)


""" Testing Ground """
# folder(combined+"09020")
# isOld(combined+"10039")
# hasSuffix(combined+"10039")
#oldStyleHunter(combined+"10039", "geotech")
#oldStyleHunter(combined+"10039", "geotech")
#oldStyleHunter(combined+"10039", "geo")
test= oldStyleHunterGeo(combined+"10039", "geo")
print(test)

# isOld(combined+"10050")
# hasSuffix(combined+"10050")


# findParents(combined)
# print(combined)
