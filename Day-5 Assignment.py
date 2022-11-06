def initializegrid(board) :
    for i in range(8) :
        for j in range(8) :
            board[i][j] = choice(['q', "r", "s", 'u', "t"])
def initialize(board) :
    initializegrid(board)
    global score
    score = 0
    global turn
    turn = 1 
def continuegame(current_score, goal_core = 100) :
    if (current_score >= goal_score):
        return False
    else:
        return True
def drawboard(board):
    linetodraw=""
    print("\n\n\n")
    print("----------------------------------")
    for i in range(7,-1,-1):
        linetodraw=""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw+= " |"
        print("line to draw")
        print("----------------------------------")
def getmove():
    print("getting move")
    return"blu"
def Update(board, move):
    print("updating board")
def doround(board):
    drawboard(board)
    move = getmove()
    Update(board, move)
    global turn
    turn += 1
score = 100
turn = 100
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
def initializegrid(board) :
    print("initializing grid")
def drawboard(board) :
    print("drawing board") 
def doround() :
    print("hello")
for i in range(100):
    i+=1
    print(i)