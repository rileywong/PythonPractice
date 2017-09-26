import sys

global people
global locations
global preferences
global preferer
global preferred
global dispreferred

def parseFile(fileName):
    f = open(fileName, 'r')
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

def generatePerference(personIndex):
	preferencesOrder = []
	for x in range(len(preferer)):
		if preferer[x]==personIndex:
			if preferred[x] in preferencesOrder:
				preferencesOrder.append(dispreferred[x])
			else:
				preferencesOrder.append(preferred[x])
				preferencesOrder.append(dispreferred[x])
	return preferencesOrder

def generateCombos(order):
	combos = []
	for x in range(len(order)-1):
		for y in range(len(order)-x-1):
			combos.append((order[x],order[y+1+x]))
	return combos
def main():
    parseFile(sys.argv[1])
    printMinimized()
    

    peoplePreferences = []
    for x in range(people):
    	peoplePreferences.append(generatePerference(x+1))

    combos = []
    for x in range(len(peoplePreferences)):
    	combos = combos + generateCombos(peoplePreferences[x])





main()
