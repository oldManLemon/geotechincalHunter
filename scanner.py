import folderRunner as bw
import os
slash = '\\'
base = "\\\sampras\\Data\\Jobs\\"
yearFolder = '2015\\'
# job = '15083'
log = open('results.txt', 'w')


def scanFolders(path):  # this is setup to scan in Bornhorstward Style
    # print(path)
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
    # print(path)
    for jobNumber in os.listdir(path):  # get job number and enter
        jobNumber = str(jobNumber)
        if(bw.hasSuffix(path+slash+jobNumber)):

            suffixes = bw.suffixDetails(path+slash+jobNumber)
             
            for suffix in suffixes:
                try:
                    print(jobNumber+suffix)
                except NotADirectoryError:
                    print('Not a directory Error')    
                                 

    log.close()      
        





scanLiveFolders(base+yearFolder)

