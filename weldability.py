#**** Finding all the edges in PRT file
# NX 1957
# Journal created by andreilo on Mon Apr 12 13:22:45 2021 W. Europe Daylight Time
#
import math
import NXOpen
from shapesNX.Block import Block
from operator import itemgetter
import NXOpen.Gateway


all_lines = []
verticals = []
temp = []
xstart = 0 #placeholders
ystart = 0
height = 0
width = 0
rectanlges = []
weldgun_size = 19 

def main() : 
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Open...
    # ----------------------------------------------
    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay("K:\\Biblioteker\\Dokumenter\\Skole\\Automatisering\\TMM4275-Assignment3\\uploadedFiles\\weldingModel.prt", NXOpen.DisplayPartOption.AllowAdditional)

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
    if v1.Z==0 and v2.Z==0: #Only use the lines that are on the base, these are the lines we potenially want to weld
        all_lines.append([round(v1.X,0),round(v1.Y,0),round(v1.Z,0),round(v2.X,0),round(v2.Y,0),round(v2.Z,0)])
    
    
def getVerticals():#makes a list of only the vertical lines, where each lines lowest point always comes before its highest point
    for line in all_lines:
        if line[0] == line[3]: #Checks if the line goes vertically
            print("Line element",line)
            if line[1] < line[4]: #To make sure the lowest point comes first
                verticals.append([line[0],line[1],line[3],line[4]]) #Only need x and y values
            elif line[1] > line[4]:
                verticals.append([line[3],line[4],line[0],line[1]])
            else:
                print("Something went wrong adding line")
    
def removeDuplicatesAndSort(list1): #The lines are sorted from left to right and duplicates are removed
    for x in list1:
        if x not in temp:
            temp.append(x)
    list1 = temp
    list1.sort(key=lambda x: x[0])
    return list1

def createRectanlges(verticals): #uses the weld lines to construct sqaures that will be colored to visulaize if it is enough room for the weldgun
    i = 0
    while i < len(verticals)-1: #loop to go through every line
        currentline = verticals[i]
        print("currentline",currentline)
        x = currentline[0] #The lowest x coordinate for the current line
        y = currentline[1] #The lowest y coordinate for the current line
        y_top = currentline[3] #The upmost y coordinate for the line
        next_y_top = 0 #The next lines top y coordinate
        next_x = 0
        foundNextLine=False #To check if there is a line orthogonal to our current line
        rectanlgetop = next_y_top #placeholder
        #We need to find the closest line to the right of current line.  The line must have a point that is horizontally on the same level as our current y starter point
        #This is the case if our current y is between the next lines top and down
        #since we have sorted all the lines from left to right, the first element will be the closest
        j=i+1
        while foundNextLine == False and j < len(verticals): #Checks all the lines after our current line to see if they are hoizontally next to our current
            if y >= verticals[j][1] and verticals[j][3] > y:
                if verticals[j][3] > y_top:
                    rectanlgetop = y_top #The rectanlge will have a top point from the top of the next line it hits
                else:
                    rectanlgetop = verticals[j][3] #We have now found the upmost point for a temporary rectanlge, but if there is a line whos lowest point is inbetween we must adjust the top of the rectanlge to this point
                next_x = verticals[j][0]
                foundNextLine = True
                print("next line",verticals[j]) 
                #Or else the rectanlge would cut through a block and that is not valid
                k = j-1
                while k > i: #Counts backwards to the current line to see find potenial lower point fir the rectanlge to begin
                    if rectanlgetop >= verticals[k][1] and verticals[k][1] > y: #If there is a line inbetween we set the rectanlgestop to this lines bottom
                        rectanlgetop = verticals[k][1]    
                    print("k",k)
                    k -= 1
            print("j",j)
            j += 1
        #If the newly found sqaure takes up the entire current line we move on to the next line. However if only a small part of the line were used
        # We now need to remove the part of the line that has a designated rectanlge to it and keep on finding rectanlges for the rest of the line
        height = rectanlgetop - y #height of the rectanlge as seen from above and down on the base
        print("rectanlgetop",rectanlgetop)
        print("y",y)
        width = next_x - x
        if height > 0 and width >0:
            rectanlges.append([x,y,width,height])
        if height == (verticals[i][3] -verticals[i][1]): #If the whole line is taken move to the next
            i += 1 
        elif height < (verticals[i][3] -verticals[i][1]):
            print("the change",verticals[i])
            verticals[i][1] = verticals[i][1] + height #If only part of the line is part of a rectanlge, move the start point of the current line up above the rectanlge and repeat loop on same index
        else:
            print("Something went wrong")
    return rectanlges

def addBlocks():
    colorstring = "YELLOW" #placeholder, if any blocks are yellow they have not gotten a color based on size
    for input in rectanlges:
        if input[2] < weldgun_size or input[3] < weldgun_size: #If the 
            colorstring = "RED"
        if input[2] >= weldgun_size and input[3] >= weldgun_size:
            colorstring = "GREEN"
        blockN = Block(input[0], input[1], 0, input[2], input[3], 1, colorstring, "Steel")
        blockN.initForNX()

def getNozzleSize():
    f = open("K:\\Biblioteker\\Dokumenter\\Skole\\Automatisering\\TMM4275-Assignment3\\variables.txt", "r") 
    size = int(f.read())
    f.close()
    return size

def saveImage():
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Fit
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Fit()
    
    scaleAboutPoint1 = NXOpen.Point3d(122.35160156613561, 129.05579891222513, 0.0)
    viewCenter1 = NXOpen.Point3d(-122.35160156613561, -129.05579891222536, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    # ----------------------------------------------
    #   Menu: File->Export->Image...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theUI = NXOpen.UI.GetUI()
    
    imageExportBuilder1 = theUI.CreateImageExportBuilder()
    
    imageExportBuilder1.RegionMode = False
    
    regiontopleftpoint1 = [None] * 2 
    regiontopleftpoint1[0] = 0
    regiontopleftpoint1[1] = 0
    imageExportBuilder1.SetRegionTopLeftPoint(regiontopleftpoint1)
    
    imageExportBuilder1.RegionWidth = 1
    
    imageExportBuilder1.RegionHeight = 1
    
    imageExportBuilder1.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Png
    
    imageExportBuilder1.FileName = "K:\\Biblioteker\\Dokumenter\\Skole\\Automatisering\\TMM4275-Assignment3\\static\\weldCheck.png"
    
    imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
    
    imageExportBuilder1.EnhanceEdges = False
    
    nXObject1 = imageExportBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId1, "Export Image")
    
    imageExportBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
        

if __name__ == '__main__':
    main()
    weldgun_size = getNozzleSize()
    getFaces()
    getVerticals()
    verticals = removeDuplicatesAndSort(verticals)
    rectanlges = createRectanlges(verticals)
    addBlocks()
    saveImage()

