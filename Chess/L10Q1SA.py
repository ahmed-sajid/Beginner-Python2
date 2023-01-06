import graphics as g

# Create the chessboard
board = g.Board()

# Create the pieces
white_king = g.Piece('white', 'king')
white_queen = g.Piece('white', 'queen')
black_king = g.Piece('black', 'king')
black_queen = g.Piece('black', 'queen')

# Place the pieces on the board
board.place_piece(white_king, (4, 0))
board.place_piece(white_queen, (3, 0))
board.place_piece(black_king, (4, 7))
board.place_piece(black_queen, (3, 7))

# Draw the initial state of the board
board.draw()

# Play the game
while True:
    # Get the next move from the player
    move = input('Enter your move: ')

    # Make the move on the board
    board.make_move(move)

    # Check for checkmate or stalemate
    if board.is_checkmate():
        print('Checkmate!')
        break
    elif board.is_stalemate():
        print('Stalemate!')
        break

    # Draw the updated state of the board
    board.draw()
