#**** Finding all the edges in PRT file
# NX 1957
# Journal created by andreilo on Mon Apr 12 13:22:45 2021 W. Europe Daylight Time
#
import math
import NXOpen
from shapesNX.Block import Block


nodes = []
corners = []
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
	print("x",v1.X)
	if v1.Z==0 and v2.Z==0:
		nodes.append([v1.X,v1.Y,v1.Z,v2.X,v2.Y,v2.Z])

def findArea():
	for i in nodes:
		for j in nodes:
			if ((i[0] == j[0]) and (i[1] == j[1]) and i!=j):
				corners.append([i[0],i[1],i[2],i[3],i[4],i[5],j[3],j[4],j[5]])
			elif((i[0] == j[3]) and (i[1] == j[4]) and i!=j):
				corners.append([i[0],i[1],i[2],i[3],i[4],i[5],j[0],j[1],j[2]])
			elif((i[3] == j[3]) and (i[4] == j[4]) and i!=j):
				corners.append([i[3],i[4],i[5],i[0],i[1],i[2],j[3],j[4],j[5]])
    
	for corner in corners:
		block_x = 0 #placeholder
		block_y = 0 #placeholder
		block_z = -100 #placeholder
		x_length = 20 #placeholder
		y_length = 20 #placeholder
		z_length = 100 #placeholder

		if (round(corner[0]) < round(corner[3])) and (round(corner[1]) < round(corner[7])):
			x_length = abs(corner[3] - corner[0])
			y_length = abs(corner[7] - corner[1])
			print("c3",corner[3])
			print("c0",corner[0])
			print("xlbbbbbbbbbb",x_length)
			print("c7",corner[7])
			print("c1",corner[1])
			print("yl",y_length)
			blockN = Block(corner[0], corner[1],corner[2]+block_z, x_length, y_length, z_length, "RED", "Steel")
			blockN.initForNX()
        #[0,1,2,3,4,5,6,7,8] corner.                                  
		if (round(corner[0]) < round(corner[6])) and (round(corner[1]) < round(corner[4])):
			x_length = abs(corner[6] - corner[0])
			y_length = abs(corner[4] - corner[1])
			print("c6",corner[6])
			print("c0",corner[0])
			print("xl",x_length)
			print("c4",corner[4])
			print("c1",corner[1])
			print("yl",y_length)
			blockN = Block(corner[0], corner[1],corner[2]+block_z, x_length, y_length, z_length, "RED", "Steel")
			blockN.initForNX()

#Getting the length of a line
def getLength(node):

        point1 = [node[0], node[1], node[2]]
        point2 = [node[3], node[4], node[5]]

        length = math.sqrt(((point1[0]-point2[0])**2)+((point1[1] - point2[1])**2))
    return length

#The gun will be represented by a block of the approximated volume
def typeOfGun(gun):
#Maybe parse the dimentions/ coordinates of the size of the block instead of the volume
#Would then be a list of the corner points of the block
    if gun == "R":
        gunSize = int
    elif gun == "D":
        gunSize = int
    elif gun == "E":
        gunSize = int
    elif gun == "F":
        gunSize = int
    
    return gunType

#Depending on the gun chosen on the website, the size is paresed to the filter.
def filteringBlock(gunSize):
    #Begins on the top left corner. Moves over the maze with a stride of one checking for obsticles.
    #If a obsticle is detected, mark the area of coverage red. 
    filterBlockN = Block(corner[0], corner[1],corner[2]+block_z, x_length, y_length, z_length, "RED", "Steel")
	filterBlockN.initForNX()
    # Can you return a NX object?
    return filterBlock

#List with corners 

if __name__ == '__main__':
	main()
	getFaces()
	print("aaaaaa",corners)
	findArea()

# Knowing what is on top, what is on the bottom, what belongs to a different body.
# To filter out edges, which "close" to two faces of different edges.
# Get intermediate edges by Z (Z = 0, in the maze.prt example)
# Finding the edges which are accessible.
