import sys
import itertools

def printMinimized(people,locations,preferences,preferer,preferred,dispreferred):

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

def generatePerference(personIndex,preferer,preferred,dispreferred):
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

def getTotalViolations(combos, locationsArr, minErrors):
	total = 0
	for x in range(len(combos)):
		if minErrors < total:
			return 99999999
		num1 = combos[x][0]
		num2 = combos[x][1]
		total = total + isViolation(num1,num2,locationsArr)
	return total

def main():

	f = open(sys.argv[1], 'r')

	preferer = []
	preferred = []
	dispreferred = []
	locations = 0

	for item in f:
		index1 = item.find('(')+1
		index2 = item.find(')')
		params = item[index1:index2].split(", ")
		if "people" in item:
			people = int(params[0])
			continue
		if "locations" in item or "places" in item:
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


	peoplePreferences = []
	for x in range(people):
		peoplePreferences.append(generatePerference(x+1,preferer,preferred,dispreferred))

	combos = []
	for x in range(len(peoplePreferences)):
		combos = combos + generateCombos(peoplePreferences[x])

	locationArray = []
	for x in range(locations):
		locationArray.append(x+1)

	minErrors = 999999
	for items in itertools.permutations(locationArray,len(locationArray)):
		minErrors = min(minErrors,getTotalViolations(combos,items,minErrors))
	print("violations("+str(minErrors)+").")



main()
