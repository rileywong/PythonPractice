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
            dish_width = [dishes]
            demand = [dishes]
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

def printMinimizedOutputs():
    print ("dishes : " + str(dishes))
    print ("separation : " + str(separation))
    print ("hot : " + str(hot))
    print ("tablewidth : " + str(table_width))
    print ("dish_width : " + str(dish_width))
    print ("demand : " + str(demand))
    for items in itertools.permutations(dish_width,len(dish_width)):
        print (items)

def main():
    parseFile(sys.argv[1])
    minimumTables()
    #printMinimizedOutputs()
    computeDemands()

main()
