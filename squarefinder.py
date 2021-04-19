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
squares = []
weldgun_size = 51

def main() : 
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------
    #basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay("K:\\Nedlastninger\\maze.prt", NXOpen.DisplayPartOption.AllowAdditional)
    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay("K:\\Biblioteker\\Dokumenter\\Skole\\Automatisering\\TMM4275-Assignment3\\maze2.prt", NXOpen.DisplayPartOption.AllowAdditional)
    
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
        all_lines.append([round(v1.X,0),round(v1.Y,0),round(v1.Z,0),round(v2.X,0),round(v2.Y,0),round(v2.Z,0)])
    
    
def getVerticals():#makes a list of only the vertical lines, where each lines lowest point always comes before its highest point
    for line in all_lines:
        if line[0] == line[3]: #Checks if the line goes vertically
            print("Line element",line)
            print("line1", line[1])
            print("line4",line[4])
            if line[1] < line[4]: #To make sure the lowest point comes first
                verticals.append([line[0],line[1],line[3],line[4]]) #Only need x and y values
                print("added1",[line[0],line[1],line[3],line[4]])
            elif line[1] > line[4]:
                verticals.append([line[3],line[4],line[0],line[1]])
                print("added2",[line[3],line[4],line[0],line[1]])
            else:
                print("Something went wrong adding line")
    
def removeDuplicatesAndSort(list1): #The lines are sorted from left to right
    for x in list1:
        if x not in temp:
            temp.append(x)
    list1 = temp
    list1.sort(key=lambda x: x[0])
    return list1

def createSquares(verticals): #uses the weld lines to construct sqaures that will be colored to visulaize if it is enough room for the weldgun
    i = 0
    test = 0
    while i < len(verticals)-1:
        test += 1
        currentline = verticals[i]
        print("currentline",currentline)
        x = currentline[0] #The x coordinate for the current line
        y = currentline[1]
        y_top = currentline[3]
        next_y_top = 0 #The next lines top y coordinate
        next_x = 0
        foundNextLine=False
        squaretop = next_y_top
        #We need to find the closest line to the right of current line.  The line must have a point that is horizontally on the same level as our current y starter point
        #This is the case if our current y is between the next lines top and down
        #since we have sorted all the lines from left to right, the first element will be the closest
        j=i+1
        while foundNextLine == False and j < len(verticals): 
            if y >= verticals[j][1] and verticals[j][3] > y:
                if verticals[j][3] > y_top:
                    squaretop = y_top
                else:
                    squaretop = verticals[j][3] #We have now found the upmost point for a temporary square, but if there is a line whos lowest point is inbetween we must adjust the top of the square to this point
                next_x = verticals[j][0]
                foundNextLine = True
                print("next line",verticals[j])
                print("current squaretop",squaretop) 
                #Or else the square would cut through a block and that is not valid
                k = j-1
                while k > i: #Counts backwards to the current line to see find potenial lower point fir the square to begin
                    if squaretop >= verticals[k][1] and verticals[k][1] > y:
                        print("verti k", verticals[k])
                        squaretop = verticals[k][1] 
                        print("Something in the middle, new top",squaretop)    
                    print("k",k)
                    k -= 1
            print("j",j)
            j += 1
        """if j == len(verticals):# If we have run through the entire list, this means there is nothing in the way. Therefor we must set the limit to the bases
            next_x = 100"""
        #If the newly found sqaure takes up the entire current line we move on to the next line. However if only a small part of the line were used
        # We now need to remove the part of the line that has a designated square to it and keep on finding squares for the rest of the line
        height = squaretop - y #height of the square as seen from above and down on the base
        print("squaretop",squaretop)
        print("y",y)
        width = next_x - x
        squares.append([x,y,width,height])
        if height == (verticals[i][3] -verticals[i][1]): #If the whole line is taken move to the next
            print("i and next",i)
            i += 1 
        elif height < (verticals[i][3] -verticals[i][1]):
            print("i and stay",i)
            print("height is",height)
            print("diff is",(verticals[i][3] -verticals[i][1]))
            print("the change",verticals[i])
            verticals[i][1] = verticals[i][1] + height #If only part of the line is part of a square, move the start point of the current line up above the square and repeat loop on same index
        else:
            print("Something went wrong")
        if test >= 30:
            break
    return squares

def addBlocks():
    colorstring = "YELLOW" #placeholder, if any blocks are yellow they have not gotten a color based on size
    for input in squares:
        if input[2] < weldgun_size or input[3] < weldgun_size:
            colorstring = "RED"
        if input[2] >= weldgun_size and input[3] >= weldgun_size:
            colorstring = "GREEN"
        blockN = Block(input[0], input[1], 0, input[2], input[3], 1, colorstring, "Steel")
        blockN.initForNX()
        

if __name__ == '__main__':
    main()
    getFaces()
    print("alllllllll lines",all_lines)
    getVerticals()
    verticals = removeDuplicatesAndSort(verticals)
    print("verticals",verticals)
    squares = createSquares(verticals)
    addBlocks()
    print("verticals",verticals)
    print("squares",squares)

