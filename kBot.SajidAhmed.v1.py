# ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   kBot_name_v1.py 
#  
#  Purpose:  This program will interact with the user and continuously tell the user a joke until otherwise made to stop.
#  It's a simple chatbot that will only tell knock knock jokes.
#  ----------------------------------------------------

import random
import sys

# This will introduce kbot and site the sources for the jokes used in the program.
def introduction():
    
    print('\n[Bot] Hi! My name is kbot. I tell KnockKnock jokes. The jokes that I tell I learned from https://www.readersdigest.ca/culture/funniest-knock-knock-jokes/')
    print()

# This will randomly pick the joke from a list 
def getjoke(c):
    joke_a = (('A little old lady','To','Saul','Ida','A broken pencil','Nobel','Boo','Luke','Leon','Police','Hatch','Van Nuys','Honeydew','KGB','Cows go','Elly','Cash','Owls','Ice cream','Dejav','Euripides','A wood wok','Spell'))
    joke_b = (('I had no idea you could yodel!','To whom.',"Saul there is. There ain't no more.","Surely it's pronounced Idaho?","Never mind. It's pointless.","No bell. That's why I knocked.","Hey, don't cry!","Luke through the peephole and find out.","Leon me … when you're not strong!","Police hurry up, it's nearly lunch time!","Bless you.","Van Nuys was 17, it was a very good year…","Honeydew you wanna dance?","We will ask the questions!","No, silly. Cows go moo!","Elly-mentary, my dear Watson!","No thanks, I'll have some peanuts.","They sure do!","Ice cream if you don't let me in!","Knock, knock.","Euripides clothes, you pay for them!","A wood wok 500 miles, and a wood wok 500 more!","Okay, fine. W-H-O."))
    index = random.randint(0,len(joke_b)-1)
    # I was sometimes getting repeat jokes so I added this just to make sure you don't get the same one twice in a row
    while c == index:
        index = random.randint(0,len(joke_b)-1)
    joke_a = joke_a[index]
    joke_b = joke_b[index]
    c = index
    return joke_a, joke_b

# This function cleans any inputted strings and strips any numbers spaces or punctuation in order to get only the letters
def cleanstring(a):
    
    b = a 
    a = []
    for y in range(len(b)):
        a.append(b[y])
    for char in a:
        if char.isspace() == True:
            a.remove(char)
    for char in a:
        if char.isalpha() == False:
            a.remove(char)
    for char in range(len(a)):
        if a[char].isalpha() == False:
            a[char] = ''
    a = ''.join(a)
    return a

#This is the main one for the dialogue exchange. It has a killswitch that activates if a certain phrase (kbot shutdown) is typed
def answerCorrectly(question,expected_response):
    you = ''
    x = -1
    expected_response_1 = expected_response
    expected_response = cleanstring(expected_response).lower()
    helpme = cleanstring("I dont know how to answer").lower()
    stop = cleanstring('kBot Shutdown').lower()
    while you != expected_response:
        if you == stop:
            sys.exit()
        if you == helpme:
            print(f'[Bot]\tHint: type "{expected_response_1}"')
        print(f'[Bot]\t{question}.')
        you = input(f'[You]\t').lower()
        you = cleanstring(you)
        x = x + 1


# main function that uses all the helper functions to build the joke loop system. 
def main():
    
    x = 0
    c = ''
    introduction()
    while x != 1:
        c = joke_a,joke_b = getjoke(c)
        answerCorrectly('Knock Knock', "Who's there?")
        answerCorrectly(joke_a,f'{joke_a} who?')
        print(f'[Bot]\t{joke_b}')
        print()
