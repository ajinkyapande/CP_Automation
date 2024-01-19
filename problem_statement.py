##Software “cp” takes two argument. src -> Source location , dst -> DestinationLocation.
## “cp” copies all content of src ->dst.
##Syntax -> cp src dst

##As a part of QA, we nee to validate if all the content of src is properly copied to dst. WRITE AUTOMATION FOR BELOW VALIDATION :
##And this includes 4 main aspects to validate :

##  - All files copied
##  - Data integrity maintained - list of corrupt files/dirs
##  - Is there any junk (file/dir) copied in dst
##  - Any missing file/dir in dst

## Use below helper methods to implement solution. DO NOT USE ANY additional libraries i.e do not import anything other than below methods in your solution.


##Helper methods (DO NOT IMPLEMENT THESE METHODS. THESE ARE AVAILABLE FOR YOU TO USE)

##-listdir(location) ->[files & dirs in current dir] (no recursive listing)
##-isfile(location) -> bool - True if file else False
##-md5sum(location) -> String - md5sum of file.


##Few tips :
##Try to build a skeleton code for modularised framework .
##Build atleast one method which can give all above result.

def listdir(location):
    from os import listdir
    return lisdir(location)

def isfile(location):
    from os.path import isfile
    return isfile(location)

def md5sum(filename):
    from hashlib import md5
    with open(filename) as fh:
        return md5(fh.read()).hexdigest()

#DO NOT IMPORT ANY library. Using above helper methods, implement your solution