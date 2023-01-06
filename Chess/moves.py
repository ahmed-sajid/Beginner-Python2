
def checkBounds(np):
    num="12345678"
    let="abcdefgh"
    if np[0] in let:
        if np[1] in num:
            return(True)
    return(False)

def checkMoved(cp,np):
    if cp[0] == np[0]:
        if cp[1] == np[1]:
            return(False)
    return(True)

def checkRookMove(cp,np):

    if(not checkBounds(np)):
        return False

    if(not checkMoved(cp,np)):
        return False

    if np[0] == cp[0]:
            return(True)
    if np[1] == cp[1]:
            return(True)
    return(False)

def checkPawnMove(cp,np,player):
    # Assume player 0 can only move up and player 1 can only move down
    if(not checkBounds(np)):
        return False
    if(not checkMoved(cp,np)):
        return False

    if player == 1:
      if int(cp[1])-1 == int(np[1]) and cp[0]==np[0]:
        return True
    elif player == 0:
      if int(cp[1])+1 == int(np[1]) and cp[0]==np[0]:
        return True

    return False

def checkKnightMove(cp,np):
    #print(cp,np)
    if(not checkBounds(np)):
        return False
    if(not checkMoved(cp,np)):
        return False

    drow = ord(cp[0]) - ord(np[0])
    dcol = int(cp[1]) - int(np[1])
    #print(drow,dcol)
    if( (abs(drow)==1 and abs(dcol)==2) or \
        (abs(drow)==2 and abs(dcol)==1) ):
        return True
    else:
        return False

def checkBishopMove(cp,np):

    if(not checkBounds(np)):
        return False
    if(not checkMoved(cp,np)):
        return False

    ncp=int(cp[1])
    nnp=int(np[1])
    cpos = nnp-ncp

    nclet=ord(cp[0])
    nnlet=ord(np[0])
    clet = nnlet-nclet

    if ( abs(cpos) == abs(clet) ) and (cpos !=0):
        return(True)
    return(False)

def checkKingMove(cp,np):

    if(not checkBounds(np)):
        return False
    if(not checkMoved(cp,np)):
        return False

    ncp=int(cp[1])
    nnp=int(np[1])
    cpos = nnp-ncp

    nclet=ord(cp[0])
    nnlet=ord(np[0])
    clet = nnlet-nclet

    if ((abs(clet)<=1) and (abs(cpos)<=1) ):
        return(True)
    return(False)

def checkQueenMove(cp,np):
    bm = checkBishopMove(cp,np)
    rm = checkRookMove(cp,np)
    km = checkKingMove(cp,np)
    if (bm or rm or km):
        return(True)
    return(False)

def fixPiece(piece):
    piece = piece.lower().strip()
    if "rook" in piece:
      return("rook")
    elif "bishop" in piece:
      return("bishop")
    elif "knight" in piece:
      return("knight")
    elif "queen" in piece:
      return("queen") 
    elif "king" in piece:
      return("king") 
    elif "pawn" in piece:
      return("pawn") 
    else:
      return(None)

def isValidMove(piece,cp,np,player):
    piece = fixPiece(piece)
    cp = cp.lower()
    np = np.lower()
    # print(piece, cp,np)
    if piece == "rook":
        return(checkRookMove(cp,np))
    elif piece == "bishop":
        return(checkBishopMove(cp,np))
    elif piece == "queen":
        return(checkQueenMove(cp,np))
    elif piece == "king":
        return(checkKingMove(cp,np))
    elif piece == "pawn":
        return(checkPawnMove(cp,np,player))
    elif piece == "knight":
        return(checkKnightMove(cp,np))
    else:
        return(None)

#if __name__ == "__main__":
    #print(checkRookMove("a7","a1"))
    #print(isValidMove("Rook","a7","a1"))

