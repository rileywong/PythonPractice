import sys
import itertools

global dishes
global separation
global hot
global table_width
global dish_width 
global demand

def parseFile(fileName):
    f = open(fileName)
    global dishes
    global separation
    global hot 
    global table_width 
    global dish_width 
    global demand 
    
    
    for item in f:
        index1 = item.find('(')+1
        index2 = item.find(')')
        params = item[index1:index2].split(", ")
        if "dishes" in item:
            dishes = int(params[0])
            dish_width = []
            demand = []
            continue
        if "separation" in item:
            separation = int(params[0])
            continue
        if "hot" in item:
            hot = int(params[0])
            continue
        if "table_width" in item:
            table_width = int(params[0])
            continue
        if "dish_width" in item:
            try:
                dish_width[int(params[0])] = int(params[1])
            except IndexError:
                dish_width.append(int(params[1]))
            continue

        if "demand" in item:
            try:
                demand[int(params[0])] = int(params[1])
            except IndexError:
                demand.append(int(params[1]))
            continue
         
def minimumTables():
    dishDict = {}

def computeDemands():
    for x in range(hot):
        dish_width[x] = str(dish_width[x]) + "h"
    for x in range(len(demand)):
        for item in range(0,demand[x]):
            dish_width.append(dish_width[x])

def printMinimizedOutputs():
    print ("dishes : " + str(dishes))
    print ("separation : " + str(separation))
    print ("hot : " + str(hot))
    print ("tablewidth : " + str(table_width))
    print ("dish_width : " + str(dish_width))
    print ("demand : " + str(demand))

def getTables(sequence,minTables):
    global dishes
    global separation
    global hot 
    global table_width 
    global dish_width 
    global demand 

    numTables = 1
    tableSize = 0

    prev = "none"
    curr = "none"
    for item in sequence:
        if(numTables > minTables):
            return 99999999
        if isinstance(item, str):
            curr = "hot"
            item = int(item[:-1])
        else:
            curr = "cold"


        if (prev != curr) and prev !="none":
            if (tableSize + separation + item) > table_width:
                numTables = numTables + 1
                prev = "none"
                tableSize = item
                continue
            else:
                prev = curr
                tableSize = tableSize + separation + item
                continue

        if (tableSize + item) > table_width:
            numTables = numTables + 1
            prev = "none"
            tableSize = item
        else:
            prev = curr
            tableSize = tableSize + item

       



    return numTables

def main():
    parseFile(sys.argv[1])
    minimumTables()
    computeDemands()
    # printMinimizedOutputs()
    mintables = 9999999
    for items in itertools.permutations(dish_width,len(dish_width)):
        #print(items)
        mintables = min(mintables,getTables(items,mintables))
    print ("tables(" + str(mintables)+").")

main()
