# events-example0.py
# Barebones timer, mouse, and keyboard events
# 15-112, Summer 2, Homework 4.2
######################################
# Full name: Samyak Kumar
# Section: C
# Andrew ID: samyakk
# Collaborated with : aavadhan
######################################


from tkinter import *
import random

####################################
# customize these functions
####################################

####################    MODEL    ####################
def init(data):

        # Seven "standard" pieces (tetrominoes)
    data.iPiece = [
    [True,  True,  True,  True]
    ]

    data.jPiece = [
    [True, False, False],
    [True, True,  True]
    ]

    data.lPiece = [
    [False, False, True],
    [True,  True,  True]
    ]

    data.oPiece = [
    [True, True],
    [True, True]
    ]

    data.sPiece = [
    [False, True, True],
    [True,  True, False]
    ]

    data.tPiece = [
    [False, True, False],
    [True,  True, True]
    ]

    data.zPiece = [
    [True,  True, False],
    [False, True, True]
    ]
    data.rows = 15
    data.cols = 10
    data.margin = 30
    data.color = "blue"
    data.board = make2dList(data.rows, data.cols, data.color)
    tetrisPieces = [ data.iPiece, data.jPiece, data.lPiece, data.oPiece, data.sPiece, data.tPiece, data.zPiece]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green",
    "orange"]
    data.tetrisPieces = tetrisPieces
    data.tetrisPieceColors = tetrisPieceColors
    # Initialize the falling piece
    newFallingPiece(data)

###############      CONTROLLERS      #######################
def newFallingPiece(data):
    # Pick a falling piece and color randomly
    fallingPiece = random.choice(data.tetrisPieces)
    fallingPieceColor = random.choice(data.tetrisPieceColors)

    data.fallingPiece = fallingPiece
    data.fallingPieceColor = fallingPieceColor

    # Position it in the middle of the screen
    data.fallingPieceRow = 0
    fallingPieceCols = len(fallingPiece[0])
    data.fallingPieceCol = data.cols//2 - fallingPieceCols//2



def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    # Make a new falling piece
    if event.keysym == "Left":
        moveFallingPiece(data, 0, -1)
    elif event.keysym == "Right":
        moveFallingPiece(data, 0, 1)
    elif event.keysym == "Down":
        moveFallingPiece(data, 1, 0)
    else:
        newFallingPiece(data)


def timerFired(data):
    pass

# Code taken from  https://www.cs.cmu.edu/~112/notes/notes-tetris/tetris-after-step-2.py
def getCellBounds(row, col, data):
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth = data.width - 2 * data.margin
    gridHeight = data.height - 2 * data.margin
    x0 = data.margin + gridWidth * col / data.cols
    x1 = data.margin + gridWidth * (col + 1) / data.cols
    y0 = data.margin + gridHeight * row / data.rows
    y1 = data.margin + gridHeight * (row + 1) / data.rows
    return (x0, y0, x1, y1)

# received this beautiful code from the course website 15-112 Fall 15
def make2dList(rows, cols, color):

    a = []
    for row in range(rows):
        a += [[color] * cols]
    return a

def moveFallingPiece(data, drow, dcol):
    # Modify the data values for the falling pieces
    # Make the first move
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    # Check if the move made is legal
    if not fallingPieceIsLegal(data):
        print("Not legal")
        # Rest the value to the previous
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol

def fallingPieceIsLegal(data):
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[row])):
            cellRow, cellCol = row + data.fallingPieceRow, col + data.fallingPieceCol
            if data.board[cellRow][cellCol] != 'blue':
                return False
            elif not inBoard(data, cellRow, cellCol):
                return False
    return True

def inBoard(data, cellRow, cellCol):
    boardTopX, boardTopY = data.margin, data.margin
    boardBottomX, boardBottomY = boardTopX + data.cols, boardTopY + data.rows
    cellCol += data.margin
    cellRow += data.margin
    print('topX, topY', boardTopX, boardTopY)
    print('bottomX, bottomY', boardBottomX, boardBottomY)
    print('cellCol, cellRow',cellCol, cellRow)
    # print(boardTopX <= cellCol <= boardBottomX)
    # print(boardTopY <= cellRow + len(data.fallingPiece[0]) <= boardBottomY)
    return boardTopX <= cellCol < boardBottomX and\
            boardTopY <= cellRow + len(data.fallingPiece[0]) < boardBottomY




#########    VIEW    ####################

def redrawAll(canvas, data):
    drawGame(canvas, data)
    pass


def drawGame(canvas, data):
    # creating background color
    canvas.create_rectangle(0, 0, data.width, data.height, fill="orange")

    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)

def drawFallingPiece(canvas, data):
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[row])):
            cell = data.fallingPiece[row][col]
            if cell:
                drawCell(canvas, row + data.fallingPieceRow,
                     col + data.fallingPieceCol, data.fallingPieceColor, data)

def drawBoard(canvas, data):
    # iterate through the board
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            drawCell(canvas,row,col,color,data)


def drawCell(canvas,row,col,color,data):

    # draw outer square
    x0,y0,x1,y1 = getCellBounds(row, col, data)
    canvas.create_rectangle(x0,y0,x1,y1,fill = "black")

    # draw inner square
    smallerMargin = int(1.000)
    canvas.create_rectangle(x0+smallerMargin,y0+smallerMargin,
    x1-smallerMargin, y1 -smallerMargin, fill = color)




####################################
# use the run function as-is
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init

    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100  # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


def playTetris():
    rows = 15
    cols = 10
    sizeBlock = 20
    margin = 30
    windowWidth = cols * sizeBlock + (2 * margin)
    windowHeight = rows * sizeBlock + (2 * margin)
    run(windowWidth, windowHeight)


playTetris()
