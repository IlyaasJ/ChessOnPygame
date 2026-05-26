import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
w, h = screen.get_size()
clock = pygame.time.Clock()
running = True

boardImg = pygame.image.load("images/board.png").convert_alpha()
boardImg = pygame.transform.scale(boardImg, (w, h))

pygame.display.set_caption("Chess")
pygame.display.set_icon(pygame.image.load("images/white-knight.png"))

# Preloading #

SQUARE_SIZE = 105
PIECE_IMAGES = {}

def load_images(square_size):
    colors = ["white", "black"]
    types = ["rook", "knight", "bishop", "queen", "king", "pawn"]
    for color in colors:
        for type in types:
            key = color + "-" + type
            img = pygame.image.load("images/" + key + ".png").convert_alpha()
            PIECE_IMAGES[key] = pygame.transform.scale(img, (square_size, square_size))

# call this once before your game loop
load_images(SQUARE_SIZE)

# Game Structure #

turn = 0 # 0 is player white, 1 is player black #

class Piece:
    def __init__(self, color, type):
        self.color = color
        self.type = type

board = [
    [Piece("black","rook"), Piece("black","knight"), Piece("black","bishop"), Piece("black","queen"), Piece("black","king"), Piece("black","bishop"), Piece("black","knight"), Piece("black","rook")],
    [Piece("black","pawn"), Piece("black","pawn"),   Piece("black","pawn"),   Piece("black","pawn"),  Piece("black","pawn"), Piece("black","pawn"),   Piece("black","pawn"),  Piece("black","pawn")],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, Piece("white", "rook"), None, None],
    [None, None, None, None, None, None, None, None],
    [Piece("white","pawn"), Piece("white","pawn"),   Piece("white","pawn"),   Piece("white","pawn"),  Piece("white","pawn"), Piece("white","pawn"),   Piece("white","pawn"),  Piece("white","pawn")],
    [Piece("white","rook"), Piece("white","knight"), Piece("white","bishop"), Piece("white","queen"), Piece("white","king"), Piece("white","bishop"), Piece("white","knight"), Piece("white","rook")],
]


# Game Functions #
def convert(i, j):
    return [(j*(h/8.1)) + 53, (i*(w/8.1)) + 53]

def DrawBoard(__board__):
    for i, row in enumerate(__board__):
        for j, piece in enumerate(row):
            if not piece: continue
            key = piece.color + "-" + piece.type
            piece.pos = convert(i, j) 
            rect = PIECE_IMAGES[key].get_rect(center=piece.pos)
            screen.blit(PIECE_IMAGES[key], rect)

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    #Update
    
    #Render
    screen.blit(boardImg, (0,0)) 
    DrawBoard(board)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
