import folderRunner as bw
import os
slash = '\\'
base = "\\\sampras\\Data\\Jobs\\"
yearFolder = '2015\\'
# job = '15083'



def scanFolders(path):  # this is setup to scan in Bornhorstward Style
    log = open('results.txt', 'w')# print(path)
    for jobNumber in os.listdir(path):  # get job number and enter
        jobNumber = str(jobNumber)
        if(bw.hasSuffix(path+slash+jobNumber)):

            suffixes = bw.suffixDetails(path+slash+jobNumber)
            for suffix in suffixes:
                # print(path+slash+jobNumber+slash+suffix)
                for dirs in os.listdir(path+slash+jobNumber+slash+suffix):
                    # print(path+slash+jobNumber+slash+suffix+slash+dirs)
                    if(bw.isOld(path+slash+jobNumber+slash+suffix)):

                        results = bw.oldStyleHunterGeo(
                            path+slash+jobNumber+slash+suffix, "geo")
                        if(len(results) > 0):
                            log.write(str(results)+"\n")
                        # log.close()
                        # print(results)

                    else:
                        results = bw.newStyleHunterGeo(
                            path+slash+jobNumber+slash+suffix, "geo")
                        if(len(results) > 0):

                            log.write(str(results)+"\n")
                        # log.close()
                        # print(results)
        else:
            if(bw.isOld(path+slash+jobNumber)):

                        results = bw.oldStyleHunterGeo(
                            path+slash+jobNumber, "geo")
                        if(len(results) > 0):
                            log.write(str(results)+"\n")
                        # log.close()
                        # print(results)

            else:
                results = bw.newStyleHunterGeo(path+slash+jobNumber, "geo")
                if(len(results) > 0):

                    log.write(str(results)+"\n")
                        # log.close()
                        # print(results)


def scanLiveFolders(path):  # this is setup to scan in Bornhorstward Style
    log = open('results.txt', 'a')# print(path)
    for jobNumber in os.listdir(path):  # get job number and enter
        jobNumber = str(jobNumber)
        if(bw.hasSuffix(path+jobNumber)): #Check if job has suffix
            systemPath = path+jobNumber
            suffixes = bw.suffixDetails(path+slash+jobNumber)
             
            for suffix in suffixes:
                systemPath = path+jobNumber+slash+suffix
                #print(systemPath)
                if(bw.isOld(systemPath)):#Test if suffix is old
                    #print(jobNumber+suffix,"is old")
                    results = bw.oldStyleHunterGeo(systemPath,'geo') #Search the old way as old is not so well defined for Geo reports
                    if(len(results) > 0):
                        log.write(str(results)+"\n")
                else:
                    if(bw.isempty(systemPath+slash+'07_REPORTS'+slash+'GEOTECH')==False): #Save Time and Resources, check only if GEOTECH folder is empty
                        #print(systemPath+slash+'07_REPORTS'+slash+'GEOTECH'+" Has stuff")
                        log.write(str(systemPath+slash+'07_REPORTS'+slash+'GEOTECH')+"\n")        
        else: #Ie this job has no Suffixes
            systemPath = path+jobNumber
            #print(systemPath, "is suffix free")
            if(bw.isOld(systemPath)):
                #print(systemPath)
                results = bw.oldStyleHunterGeo(systemPath,'geo') #It looks for docs first so if it is just a corresp folder it will be ignored
                if(len(results)>0):
                    log.write(str(results)+"\n")
            else:
                if(bw.isempty(systemPath+slash+'07_REPORTS'+slash+'GEOTECH')==False):
                    #print(systemPath+slash+'07_REPORTS'+slash+'GEOTECH'+" Has stuff")
                    log.write(str(systemPath+slash+'07_REPORTS'+slash+'GEOTECH')+"\n")  

                                 

    log.close()      
        





#scanLiveFolders(base+yearFolder)

