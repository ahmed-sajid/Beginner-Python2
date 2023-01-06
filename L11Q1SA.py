#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L10Q1SA.py
#  
#  Purpose:   This program will determine certain times on the planet Ork.
#  ----------------------------------------------------
import pickle

#Purpose: Translation Class

class Translation:
    #Purpose: initializes everything
    #Parameter: self, tkey(string)
    #Return None
    def __init__(self,tkey = 'en-cr'):
        self.tkey = tkey
        name = str(f'dictionary-{tkey}.pkl')
        self.filename = name
        self.data = self.loadData()
            
       
    #Purpose: main translayte function
    #  Parameter: old(str), en/cree (list of words)
    #Return new(str) or string(Str)
    def translate(self,old,en = '',cree = ''):
        pairs = []
        try:
            if old in en:
                index = en.index(old)
            new = cree[index]
            return new
        except:
            string = ('Error finding key or dictionary, try again')
            KeyError
            return string
    #Purpose: Loads data from file 
    #Parameter: 
    #Return data
    def loadData(self):
        try:
            file = open(self.filename,'rb')
        except:
            data = {}
            return data
        data = pickle.load(file)
        return data
    #Purpose: Add entry to your main dictionary
    #pararm none
    # return none
    def addEntry(self,old,new):
        self.data.update({old:new})
        return
    #Purpose: Saves data to new file
    #Parameter: none
    #Return none
    def saveData(self):
        try:
            file = open(self.filename,'wb')
        except:
            print('Error')
        pickle.dump(self.data,file)
    def delete(self,old):
        try:
            self.data.pop(old)
        except:
            KeyError
    
        
            
        
        
    #Purpose: tells length of a given input
    #Parameter: none
    #Return x(list)
    def len(self):
        x = []
        for i in (self):
            x.append(len(i))
        return x
#Purpose: Main function puts it all together
#Parameter: none
#Return none
def main():
    t1 = Translation()
    en = 'walk sleep cry painful buck gun clock land fight eats'.split()
    cree = 'pimohtew nipâwin kâkîtwêw âhkwan iyâpêw apisci-pâskisikanis opîsimohkânimiw âhtaskêw mâsihêw mowêw'.split()
    for x in range(len(en)):
        t1.addEntry(en[x],cree[x])
    keys = (t1.data.keys())
    string = (f'Length : {len(t1.data)}\nEnglish Entries:\n ')
    ctring = 'Cree Translations:\n '
    for x in t1.data.items():
        ctring = ctring + f'{x[1]}: {x[0]}\n '
        string = string + f'{x[0]}: {x[1]}\n '
    print(string)
    print(ctring)
    
main()



    