
import os

# base = "\\\hawkeye\\archive\\"
# yearFolder = '2013\\'
base = "\\\sampras\\Data\\Jobs\\"
yearFolder = '2015\\'
# job = '15083'
combined = base+yearFolder

slash = '\\'

def isempty(path):
    """ 
    Check if directory passed contains files
    Args: 
        path(str)
    Returns: bool (True if empty)
     """
    print(path)
    if(len(os.listdir(path))==0):
        print("True")
        return True
    else: 
        print("False")
        return False




def hasSuffix(path):
    """ Check to see if job has suffixes attached.

    Args:
        path(str)
    Returns: Returns bool  
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
        #print(suffixList)
        return True
    else:
        False

def suffixDetails(path):
    suffixList = []
    #print(path)
    for dirs in os.listdir(path):
        if(os.path.isdir(path+slash+dirs)):
            if(dirs.startswith('_')):
                suffixList.append(dirs)
    if(len(suffixList) > 0):
        return suffixList


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
                #print("False, ie it is new", dirs)
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
              
def newStyleHunterGeo(path, searchTerm):
    """ New style folder scanner and hunter
    Args:
        File path (str)
        Searchable Object (str)

    Returns: 
        Returns an array

     """

    #print(path, searchTerm)
    location=[]
    #print(path)
    for dirs in os.listdir(path):
        if(dirs.startswith("07_")):#Limits search directory. Also ignores Suffixes
            #print(path+slash+dirs)
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
        # if(isOld(path+jobNumber)):
            # print(jobNumber,"OLD")
        # else: 
            # print(jobNumber, "NEW")


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


#test= oldStyleHunterGeo(combined+"13375", "geo")
#test= newStyleHunterGeo(combined+"13375", "fee")
#print(test)

# isOld(combined+"10050")
# hasSuffix(combined+"10050")


#findParents(base+yearFolder)
# print(combined)


#isempty(combined+"15042"+slash+"07_Reports"+slash+"DESIGNREPORTS")