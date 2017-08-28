### hangman

import os
import time
from random_words import RandomWords

os.system("clear") # clears the terminal

rw = RandomWords()
word = rw.random_word() # saves a random word

lenght = len(word)
spaces = list("_" * lenght)
space_str = "".join(spaces)
tries = 5
correct_ans = []
ans = []
correct = list(word)
ordering = {}
print "WELCOME TO THE *HANGMAN* GAME.\n"
time.sleep(1)
print "Type 'help' for the in-game help screen."
print "\nThe command 'tries' gives you how many tries you got left."
print "\nThe command 'cheats' gives you the answer."
print "\nThe command 'order' gives you the order of the letters on the word."
print "\n\n\n\n\n\n\n\n\n\t\t\tLOADING..."
time.sleep(1.8)
if raw_input("Press ENTER if you read the rules already.") == "":
    time.sleep(0)
else:
    time.sleep(8)
os.system("clear")
print "The word is " + str(lenght) + " spaces long."

while tries > 0:
    answer = raw_input("\nType a letter > ").lower()

    if answer == "help":
        print """
        Instructions:
        _______________________________________________________________
        You have to type a letter each time untill you find
        the full word. It doesn't have to be in the right order for you
        to win.

        If you type 'cheats' you can see the word.
        If you type 'tries' you can see how many tries you have left.
        If you type 'order' you can see the order of the letters on the word."""

    elif answer == "tries":
        print "You have " + str(tries) + " tries left."

    elif answer == "cheats":
        print "The magic word is " + "'" + word + "'" + "."

    elif answer == "order":
        print "The word has " + str(lenght) + " letters.\n\n"
        if correct_ans == []:
            print "You haven't guessed yet."
        else:
            if correct[0] in correct_ans:
                print "This letter " + "'" + correct[0] + "'" + " is in the 1st position."
        if correct[1] in correct_ans:
            print "This letter " + "'" + correct[1] + "'" + " is in the 2nd position."
        if correct[2] in correct_ans:
            print "This letter " + "'" + correct[2] + "'" + " is in the 3rd position."
        for i in range(3, lenght):
            if correct[i] in correct_ans:
                print "This letter " + "'" + correct[i] + "'" + " is in the " + str(i + 1) + "th position."

    elif answer in correct:

        ans += answer
        correct_ans += answer
        tries += 1
        os.system("clear")
        print "\n\n\n\n$$$$$$$$$$$$$$\nYOU GOT ONE!\n$$$$$$$$$$$$$$\n"
        time.sleep(0.5)
        print "This are the answers you got so far:"
        print "\t" + "/".join(ans).upper()
        print "\n\nThis word has " + str(word.count(answer)) + " letter(s) " + "'" + answer + "'" + " in it."

        for i in range(0, 3):
            if answer == correct[0]:
                print "This letter is in the 1st position."
                if answer != correct[1] and answer != correct[2]:
                    break
            elif answer == correct[1]:
                print "This letter is in the 2nd position."
                if answer != correct[2]:
                    break
            elif answer == correct[2]:
                print "This letter is in the 3rd position."
                break
        if lenght >= 3:
            for i in range(3, lenght):
                if answer == correct[i]:
                    print "This letter is in the " + str(i + 1) + "th position."

        if word.count(answer) == correct_ans.count(answer):
            print "\n\tYou found all the " + "'" + answer + "' letter(s) in the word."

        elif correct_ans.count(answer) > word.count(answer):
            print "\nThat's too many " + "'" + answer + "' letter(s)."
            correct_ans.remove(answer)
            tries -= 1

        print "\nThis are the CORRECT answers you got so far:"
        print "\t" + "/".join(correct_ans).upper()
        print "\n\t\tIt's your turn again.\n"
        answer = ""

    else:
        os.system("clear")
        print "\n##########\nTRY AGAIN...\n##########\n"
        time.sleep(0.5)
        os.system("clear")
        ans += answer
        print "\nThis are the answers you got so far:"
        print "\t" + "/".join(ans).upper() + "\n"
        print "This are the CORRECT answers you got so far:"
        print "\t" + " / ".join(correct_ans).upper()
        tries += -1

        if correct_ans == []:
            print "\tYou have no correct answers."


    if sorted(correct_ans) == sorted(correct):

        while tries > 0:
            print "You have " + str(tries) + " left. Type carefully."
            print "Type the correct word:"
            final = raw_input("")

            if final == word:
                tries = -1

            else:
                tries += -1

if tries == 0:
    print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\tYou lost, sorry!\n\t\t\t\tThe word was " + "'" + word + "'.\n\n\n\n\n\n\n\n\n\n"

else:
    os.system("clear")
    for i in range(3):
        print """

                 ****  **** ****** **  **
                    ****    **  ** **  **
                     **     **  ** **  **
                     **     ****** ******

              """
        time.sleep(0.5)
        print """

                 ****              ****  ******  ****  **
                  ****   ****    ****    **  **  ** ** **
                    *** *** *** ***      **  **  **  ****
                     *****   *****       ******  **   ***

              """
        time.sleep(0.8)
        os.system("clear")
    time.sleep(0.3)
    print "\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t***YOU WON!***\n\t\t\t\tThe word was " + "'" + word + "'.\n\n\n\n\n\n\n\n\n\n"
