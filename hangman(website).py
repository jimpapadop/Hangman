import sys
import urllib.request

word = input("enter a word:")
listw = [] #this list is filled with the letters of the word
listp = [] #this list is filled with len(word)*-
listlettersgiven = [] #in this list are inserted all the letters given
c2 = 0
c1 = 0
c4 = 20
lives = 6

while c2 != len(word):        #insert letters to listw
    listw.insert(c2, word[c2])
    c2 += 1

data = urllib.request.urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt").read() #in this site exist an english dictionary so that the programm can check if your input is valid

if word in str(data):
    print("")
else :
    print("-this word does not exist, please pick another one")
    sys.exit()

while c4 != 0: #this is used in order to hide the word from the player 2
    print(' ')
    c4 -= 1

print("Your goal is to find the hidden word")
print("You have 6 lives")


while c1 != len(word):   #create list with "--"
 listp.insert( c1 ,"-" )
 c1 += 1


while lives != 0:
 letter_given = input("give a guess:")
 if len(letter_given) > 1 :                                  #checking for various errors
     print('--you can only enter one letter at a time--')
 elif len(letter_given) == 0:
     print("--please insert a letter--")
 elif letter_given.isdigit():
     print("--you can only insert letters--")
 elif not letter_given.isalnum() :
     print("--you can only insert letters--")
 else:
  if letter_given in listlettersgiven:
     print("--You have already given this letter,choose another one--")
  else:                                         #if letter given is correct it goas here
    listlettersgiven.insert(0,letter_given)
    if letter_given in listw :
        print("correct guess")
        for c3 in range(len(listw)):
          if listw[c3] == letter_given:
            listp[c3] = letter_given
            listring = ''.join(map(str, listp))
            print(listring)
            if listw== listp:
                print("\033[01;46m""You Found It")
                sys.exit()


    else :                                        #if letter given is wrong it goas here
        listlettersgiven.insert(0, letter_given)
        lives-=1
        if lives !=1 :
          print("you have" ,lives, "lives")
        else:
          print("you have", lives, "live")
        print("try another letter")
        listring = ''.join(map(str, listp))
        print(listring)

if lives == 0:
    print("\033[01;41m""Better luck next time")









