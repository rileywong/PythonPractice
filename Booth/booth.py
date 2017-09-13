import sys

global grid

def parseFile(fileName):
    f = open(fileName)
    for item in f:
        index1 = item.find('(')+1
        index2 = item.find(')')
        params = item[index1:index2].split(", ")
        print(params)
        if "room" in item:
            grid
            print ("room : " + params[0] + params[1])
            continue
        if "booths" in item:
            print ("booths : " + params[0])
            continue
        if "dimension" in item:
            print ("dimension: " + params[0] + params[1] + params[2])
            continue
        if "position" in item:
            print("position: " + params[0] + params[1] + params[2])
            continue
        if "target" in item:
            print("target : " + params[0] + params[1] + params[2])
            continue

def main():
    parseFile(sys.argv[1])

main()
