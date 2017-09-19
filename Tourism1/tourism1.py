import sys

global people
global locations
global preferences
global preferer
global preferred
global dispreferred

def parseFile(fileName):
    f = open(fileName)
    global people
    global locations
    global preferences
    global preferer
    global preferred
    global dispreferred
    preferer = []
    preferred = []
    dispreferred = []
    
    for item in f:
        index1 = item.find('(')+1
        index2 = item.find(')')
        params = item[index1:index2].split(", ")
        if "people" in item:
            people = int(params[0])
            continue
        if "locations" in item:
            locations = int(params[0])
            continue
        if "preferences" in item:
            preferences = int(params[0])
            continue
        if "order" in item:
            preferer.append(int(params[0]))
            preferred.append(int(params[1]))
            dispreferred.append(int(params[2]))
            continue

    
def printMinimized():
    print ("people : " + str(people))
    print ("locations : " + str(locations))
    print ("preferences : " + str(preferences))
    print ("preferer : " + str(preferer))
    print ("preferred : " + str(preferred))
    print ("dispreferred : " + str(dispreferred)) 

def isViolation(num1,num2,sequence):
    x = sequence.index(num1)
    y = sequence.index(num2)
    if x < y:
        return 0
    else:
        return 1

def main():
    parseFile(sys.argv[1])
    printMinimized()
    


main()
