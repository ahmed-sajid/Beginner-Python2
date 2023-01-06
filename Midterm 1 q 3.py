
def randalpha(x):
    
    alphabet = ' a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    listt = []
    import random
    for i in range(0,x):
        num = random.randint(0,len(alphabet)) - 1
        index = alphabet[num]
        listt.append(index)
    return listt
    


def createUUID():
    import random
    listt = randalpha(16)
    
    for i in range(0,16):
        num = random.randint(0,9)
        listt.append(num)
    for i in range(8):
        ran = random.randint(0,len(listt))
        print(listt[ran],end = '')
    print('-',end = '')
    for i in range(4):
        ran = random.randint(0,len(listt))
        print(listt[ran],end = '')
    for i in range(4):
        ran = random.randint(0,len(listt))
        print(listt[ran],end = '')
    print('-',end = '')
    for i in range(4):
        ran = random.randint(0,len(listt))
        print(listt[ran],end = '')
    print('-',end = '')
    for i in range(8):
        ran = random.randint(0,len(listt))
        print(listt[ran],end = '')
(createUUID())
    

