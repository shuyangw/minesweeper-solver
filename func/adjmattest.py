import os
import numpy

#List of edges
edges = []

#Adjacency Matrix w/ numpy
adjMat = numpy.zeros(shape=(0,0))

def runDebug():
    cardV, cardE = parseRawFile("nonbip2", False)
    initAdjMat(cardV, cardV)
    testMat()

#Adds edges to edges field, returns cardE and cardV
def parseRawFile(filename, zeroIndex):
    #Change current working dir to the root folder of bfsengine.py
    currpath = os.path.abspath(__file__)[:-13] #Removes the bfsengine.py part of path string
    os.chdir(currpath)
    cwd = os.getcwd()

    cardE = 0
    cardV = 0
 
    #Parses the file, adds edges to edges list
    with open(os.path.join("testfiles", filename), "r") as f:
        for line in f:
            currline = line.split( )
            if(len(currline) == 1):
                cardV = int(currline[0])
            else:
                currline[0] = int(currline[0])
                currline[1] = int(currline[1])
                if zeroIndex == False:
                    edges.append((currline[0]-1, currline[1]-1))
                else:
                    edges.append((currline[0], currline[1]))
                cardE += 1
    return cardV, cardE
def initAdjMat(dimN, dimM):
    global adjMat
    adjMat = numpy.zeros(shape = (dimN, dimM))
def testMat():
    for edge in edges:
        adjMat[int(edge[0]), int(edge[1])] = True
        adjMat[int(edge[1]), int(edge[0])] = True
    print (adjMat)

