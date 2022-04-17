from random import randint
from string import ascii_uppercase, ascii_lowercase
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Centering message
def center(msg, count=False):
    try:
        w = os.get_terminal_size()[0]
        if w > (len(msg) + 1):
            spaceCount = int((w - len(msg)) / 2)
            msg = " " * spaceCount + msg
            if count: return spaceCount
            else: return msg
        else:
            if count: return 0
            else: return msg
    except OSError:
        if count: return 0
        else: return msg


def centerToTab():
    return " " * center("+-------+-------+-------+-------+-------+", True)


def centerToLtrs():
    return " " * center(" ".join(ascii_uppercase), True)


# Globals ◼
ltrs = dict.fromkeys(ascii_uppercase, 0)
allWords = open(resource_path('src/words.txt')).read().splitlines()
allowedWords = open(resource_path('src/allowed.txt')).read().splitlines()


# Clearing screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Pausing
def pause(msg="Press Enter to continue . . . "):
    input("\n" + center(msg))


# Choosing random word from file
# noinspection PyDefaultArgument
def pickWord(usedList=[""]*20):
    # Reading words.txt and making empty choice variable
    global allWords
    chosen = ""

    # Selecting random word
    while chosen in usedList:
        chosen = allWords[randint(0, len(allWords))]

    # Adding word to used
    usedList = usedList[1:]
    usedList.append(chosen)

    return chosen, usedList


# Check letter is right or at least in word somewhere
def checkRight(word, ans, ind):
    word = word.lower()

    # Check letter is right
    if word[ind] == ans[ind]:
        ltrs[word[ind].upper()] = 3
        return "**"

    # Dictionary tracking cumulative wrong position letter counts
    ltrNums = dict.fromkeys(ascii_lowercase, 0)

    # Otherwise, check if it is in the word anywhere (That isn't already correct)
    for i in range(len(ans)):
        if i == ind:
            ltrNums[word[i]] += 1

            # Checking for case when multiple similar guesses are not in the right place
            freeLtrs = 0
            for j in range(len(ans)):
                if (ans[j] == word[ind]) and (word[j] != ans[j]):
                    freeLtrs += 1

            if freeLtrs >= ltrNums[word[ind]]:
                if ltrs[word[ind].upper()] != 3: ltrs[word[ind].upper()] = 2
                return "()"
            else:
                break
        elif word[i] != ans[i]:
            ltrNums[word[i]] += 1

    # If neither case is true (Letter is wrong)
    if ltrs[word[ind].upper()] < 2: ltrs[word[ind].upper()] = 1
    return "--"


def drawRow(word, ans):
    if word == "":
        return ("\n" + centerToTab() + "|       |       |       |       |       |" +
                "\n" + centerToTab() + "+-------+-------+-------+-------+-------+")
    else:
        word = word.upper()
        return ("\n" + centerToTab() +
                f"| {checkRight(word, ans, 0)[0]} {word[0]} {checkRight(word, ans, 0)[1]} " +
                f"| {checkRight(word, ans, 1)[0]} {word[1]} {checkRight(word, ans, 1)[1]} " +
                f"| {checkRight(word, ans, 2)[0]} {word[2]} {checkRight(word, ans, 2)[1]} " +
                f"| {checkRight(word, ans, 3)[0]} {word[3]} {checkRight(word, ans, 3)[1]} " +
                f"| {checkRight(word, ans, 4)[0]} {word[4]} {checkRight(word, ans, 4)[1]} |" +
                "\n" + centerToTab() +
                "+-------+-------+-------+-------+-------+")


# noinspection PyDefaultArgument
def drawBoard(ans, words=[""]*6):
    board = center("+-------+-------+-------+-------+-------+")

    for i, word in enumerate(words):
        board += drawRow(word, ans)

    return board


def printError(msg):
    print(center("!!! ERROR:" + msg.upper() + " !!!"))
    pause()


def gameEnd(ans, word, t):
    if word == ans:
        msg = center("*** YOU WON ***") + "\n"
    else:
        msg = center("--- YOU LOST ---") + "\n"
        msg += center(f"Correct answer was {answer.upper()}") + "\n"

    msg += center(f"Turns taken: {t}/6") + "\n"

    print(msg)
    pause("Press Enter to play again . . . ")


def printLtrs():
    msg = centerToLtrs()
    for ltr in ascii_uppercase:
        msg += ["  ", "X ", "~ ", "* "][ltrs[ltr]]

    msg += "\n" + center(" ".join(ascii_uppercase))
    print(msg)


def printDebug(msg):
    print(center("### DEBUG: " + msg + " ###"))
    pause()


def printHelp(cheats):
    msg = (
        center("### HELP MENU ###") + "\n" +
        centerToLtrs() + "[Commands]\n" +
        centerToLtrs() + "\\q       - Quits the whole game\n" +
        centerToLtrs() + "\\r       - Restarts the game\n" +
        centerToLtrs() + "\\cheats  - Activates debug mode"
    )
    
    if cheats:
        msg += (
            "\n\n" +
            centerToLtrs() + "[Debug Commands]\n" +
            centerToLtrs() + "\\ans     - Returns the answer to the current puzzle\n" +
            centerToLtrs() + "\\used    - Returns a list of the past 20 used words"
        )

    print(msg)
    pause()


### Game ###
running = True
debug = False

# Picking first word
answer, used = pickWord()

while running:
    playing = True
    wordList = [""]*6
    turn = 0
    ltrs = dict.fromkeys(ascii_uppercase, 0)

    while playing:
        cls()
        print(drawBoard(answer, wordList))
        printLtrs()
        inp = input(" " * center("+-------+-------+-------+-------+-------+", True) + "> ")

        ### Commands ###
        # Checking help menu PLACEHOLDER
        if inp.lower() == "\\help":
            printHelp(debug)
        # Quitting game
        elif inp.lower() == "\\q":
            playing = False
            running = False
            break
        # Restarting game
        elif inp.lower() == "\\r":
            playing = False
            break
        ### Debug ###
        elif inp.lower() == "\\cheats":
            debug = not debug
            printDebug(f"Debug is now {['OFF', 'ON'][debug]}")
        elif debug and (inp.lower() == "\\ans"):
            printDebug(f"Answer is: {answer.upper()}")
        elif debug and (inp.lower() == "\\used"):
            printDebug(f"Words used are: {used}")
        ### Wrong input checks ###
        elif len(inp) != 5:
            printError("Input not of length 5")
        elif not inp.isalpha():
            printError("Input must be letters only")
        elif inp.lower() not in allowedWords + allWords:
            printError("Not a valid word")
        elif inp in wordList:
            printError("Already used that word")
        ### Correct user input ###
        else:
            wordList[turn] = inp
            turn += 1

            # Checking if game is over
            if (turn > 5) or (inp == answer):
                cls()
                print(drawBoard(answer, wordList))
                gameEnd(answer, inp, turn)

                playing = False
                break

    # Picking next word
    answer, used = pickWord(used)
