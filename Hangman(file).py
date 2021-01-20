import sys

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

with open('words_alpha.txt') as word_file:     #we check if the word given is valid with a file
    valid_words = set(word_file.read().split())
found = False
for each_word in valid_words:
    if word == each_word:
        found = True
        break
if found:
    print("")
else:
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

listring = ''.join(map(str, listp))
print(listring)

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
  else:                                         #if letter given is correct it goes here
    listlettersgiven.insert(0,letter_given)
    if letter_given in listw :
        print("correct guess")
        for c3 in range(len(listw)):
          if listw[c3] == letter_given:
            listp[c3] = letter_given
            listring = ''.join(map(str, listp))
            if listw == listp:
                print(listring)
                print("\033[01;46m""You Found It")
                sys.exit()
        print(listring)


    else :                                        #if letter given is wrong it goes here
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


















