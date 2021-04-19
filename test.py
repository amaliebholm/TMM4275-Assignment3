verticals = [[-585.0, -48.0, -585.0, 29.0], [-548.0, 29.0, -548.0, 361.0], [-548.0, -365.0, -548.0, -48.0], [-548.0, -48.0, -548.0, 29.0], [-88.0, -365.0, -88.0, -426.0], [-88.0, -365.0, -88.0, -48.0], [-88.0, 361.0, -88.0, 398.0], [-88.0, 29.0, -88.0, 361.0], [43.0, 398.0, 43.0, 361.0], [43.0, 29.0, 43.0, 361.0], [43.0, -426.0, 43.0, -365.0], [43.0, -365.0, 43.0, -48.0], [571.0, 29.0, 571.0, 172.5], [571.0, -48.0, 571.0, 29.0], [571.0, -172.5, 571.0, -48.0], [621.0, 172.5, 621.0, 361.0], [621.0, -365.0, 621.0, -172.5], [636.0, -48.0, 636.0, 29.0]]
#verticals = [[0,0,0,4],[1,0,1,4],[4,0,4,1],[4,3,4,4],[6,0,6,4]]
xstart = 0 #placeholders
ystart = 0
height = 0
width = 0
squares = []


def createSquares(): #uses the weld lines to construct sqaures that will be colored to visulaize if it is enough room for the weldgun
    i = 0
    test = 0
    while i < len(verticals)-1:
        test += 1
        print("i",i)
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
            print("i and next")
            i += 1 
        elif height < (verticals[i][3] -verticals[i][1]):
            print("i and stay")
            print("height is",height)
            print("diff is",(verticals[i][3] -verticals[i][1]))
            print("the change",verticals[i])
            verticals[i][1] = verticals[i][1] + height #If only part of the line is part of a square, move the start point of the current line up above the square and repeat loop on same index
        else:
            print("Something went wrong")
        if test >= 30:
            break
    return squares

if __name__ == '__main__':
    createSquares()
    print("squares",squares)