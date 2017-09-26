import sys
import itertools

def printMinimized(people,locations,preferences,duration,openTime,closeTime,preferer,preference):
	print("people : " + str(people))
	print("locations : " + str(locations))
	print("preferences : "  + str(preferences))
	print("duration : " + str(duration))
	print("open : " + str(openTime ))
	print("close : " + str(closeTime))
	print("preferer : " + str(preferer))
	print("preferences : " + str(preference ))

def getPreferences(person,preferer,preference):
	prefSequence = []
	for x in range(len(preferer)):
		if preferer[x] == person:
			prefSequence.append(preference[x])
	return prefSequence

def getVisitedPlaces(sequence,duration,openTime,closeTime):
	timeFrame = []

	minTime = min(openTime)
	maxTime = max(closeTime)

	for x in range(minTime,maxTime):
		timeFrame.append(x)

	stop = 0
	placesVisited = []

	for x in range(len(sequence)):
		if stop == 1:
			break
		index = openTime[sequence[x]] % minTime
		visitDuration = duration[sequence[x]]
		
		for y in range(openTime[sequence[x]],closeTime[sequence[x]]):
			# print("THIS IS FOR TIME + " + str(sequence[x]))
			# print(timeFrame)
			if timeFrame[y%openTime[sequence[x]] + (openTime[sequence[x]]-minTime)] != -1:

				visitDuration = visitDuration-1
				timeFrame[y%openTime[sequence[x]]+ (openTime[sequence[x]]-minTime)] = -1
				# print("AFTER THE CHANGE " + str(timeFrame)) 
				if visitDuration == 0:
					break
			else:
				next

		if visitDuration != 0:
			stop = 1
		else:
			placesVisited.append(sequence[x])
			
	return placesVisited

def getSatisfaction(prefPP,visitedPlaces,locations):
	numSatis = 0
	for x in prefPP:
		if x in visitedPlaces:
			numSatis = numSatis +1

	if numSatis == len(prefPP):
		numSatis = locations

	return numSatis

def main():

	f = open(sys.argv[1], 'r')

	people = 0
	locations = 0
	preferences = 4
	duration = []
	openTime = []
	closeTime = []
	preferer = []
	preference = []

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
		if "location" in item or "place" in item:
			duration.append(int(params[1]))
			openTime.append(int(params[2]))
			closeTime.append(int(params[3]))
			continue
		if "prefer" in item:
			preferer.append(int(params[0]))
			preference.append(int(params[1]))
			continue

	# printMinimized(people,locations,preferences,duration,openTime,closeTime,preferer,preference)

	preferencePerPerson = []
	for x in range(people):
		preferencePerPerson.append(getPreferences(x+1,preferer,preference))

	locationArray = []
	for x in range(locations):
		locationArray.append(x)

	
	minSatisArray = []
	for items in itertools.permutations(locationArray,len(locationArray)):
		
	 	minSats = []
	 	for prefPP in preferencePerPerson:
	 		visitedPlace = getVisitedPlaces(items,duration,openTime,closeTime)
	 		minSats.append(getSatisfaction(prefPP,visitedPlace,locations))
	 	minSatisArray.append(min(minSats))

	print("satisfaction("+str(max(minSatisArray))+").")
	# print(getSatisfaction([1,2,3],[6,3,1,2],10))	
	# print(getSatisfaction([1,2,3],[6],10))				


main()
















