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

	printMinimized(people,locations,preferences,duration,openTime,closeTime,preferer,preference)





main()
