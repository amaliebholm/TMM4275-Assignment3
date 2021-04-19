#**** Finding all the edges in PRT file
# NX 1957
# Journal created by andreilo on Mon Apr 12 13:22:45 2021 W. Europe Daylight Time
#
import math
import NXOpen
from shapesNX.Block import Block
from operator import itemgetter


all_lines = []
verticals = []
temp = []
xstart = 0 #placeholders
ystart = 0
height = 0
width = 0

def main() : 
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------
    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay("K:\\Nedlastninger\\maze.prt", NXOpen.DisplayPartOption.AllowAdditional)
    
    workPart = theSession.Parts.Work # maze
    displayPart = theSession.Parts.Display # maze
    partLoadStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------

def getFaces():
    theSession  = NXOpen.Session.GetSession()
    #workPart = theSession.Parts.Work
        
    for partObject in theSession.Parts:
        processPart(partObject)
        
def processPart(partObject):
    for bodyObject in partObject.Bodies:
        processBodyFaces(bodyObject)
        #processBodyEdges(bodyObject)
            
def processBodyFaces(bodyObject):
    for faceObject in bodyObject.GetFaces():
        processFace(faceObject)
            
def processFace(faceObject):
    print("Face found.")
    for edgeObject in faceObject.GetEdges():
        processEdge(edgeObject)
        
def processEdge(edgeObject):
    #Printing vertices
    v1 = edgeObject.GetVertices()[0]
    v2 = edgeObject.GetVertices()[1] 
    print("Vertex 1:", v1)
    print("Vertex 2:", v2)
    if v1.Z==0 and v2.Z==0: #Only use the lines that are on the base
        all_lines.append([round(v1.X,2),round(v1.Y,2),round(v1.Z,2),round(v2.X,2),round(v2.Y,2),round(v2.Z,2)])
    
    
def getVerticals():#makes a list of only the vertical lines, where each lines lowest point always comes before its highest point
    for line in all_lines:
        if line[0] == line[3]: #Checks if the line goes vertically
            #print("Line element",line)
            if line[1] < line[3]: #To make sure the lowest point comes first
                verticals.append([line[0],line[1],line[3],line[4]]) #Only need x and y values
                #print("added",[line[0],line[1],line[3],line[4]])
            elif line[1] > line[3]:
                verticals.append([line[3],line[4],line[0],line[1]])
                #print("added",[line[3],line[4],line[0],line[1]])
            else:
                print("Something went wrong adding line")
    
def removeDuplicatesAndSort(list1): #The lines are sorted from left to right
    for x in list1:
        if x not in temp:
            temp.append(x)
    list1 = temp
    list1.sort(key=lambda x: x[0])
    return list1

def createSquares(): #uses the weld lines to construct sqaures that will be colored to visulaize if it is enough room for the weldgun
    while i < (len(verticals) - 1)


if __name__ == '__main__':
    main()
    getFaces()
    getVerticals()
    verticals = removeDuplicatesAndSort(verticals)
    print("aaaaaaaa",all_lines)
    print("verticals",verticals)
    

