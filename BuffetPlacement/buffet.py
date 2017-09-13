import sys

global grid

def parseFile(fileName):
    f = open(fileName)
    for item in f:
        index1 = item.find('(')+1
        index2 = item.find(')')
        params = item[index1:index2].split(", ")
        print(params)
        if "dishes" in item:
            print ("dishes : " + params[0])
            continue
        if "separation" in item:
            print("separation : "params[0])
            continue
        if "hot" in item:
            print("hot : "params[0])
            continue
        if "table_width" in item:
            print ("table_width : " + params[0])
            continue
        if "dish_width" in item:
            print (params[0] + params[1])
            continue
        if "demand" in item:
            print (params[0] + params[1])
            continue
        
def main():
    parseFile(sys.argv[1])

main()
