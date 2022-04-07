from random import randint
from time import sleep
from string import ascii_uppercase, ascii_lowercase


# Globals
ltrs = dict.fromkeys(ascii_uppercase, 0)


# Choosing random word from file
# noinspection PyDefaultArgument
def pickWord(usedList=[""]*20):
    # Reading words.txt and making empty choice variable
    lines = open('words.txt').read().splitlines()
    chosen = ""

    # Selecting random word
    while chosen in usedList:
        chosen = lines[randint(0, len(lines))]

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
                print(ans, word, ind, freeLtrs, ltrNums[word[ind]])
                break
        elif word[i] != ans[i]:
            ltrNums[word[i]] += 1

    # If neither case is true (Letter is wrong)
    if ltrs[word[ind].upper()] < 2: ltrs[word[ind].upper()] = 1
    return "--"


def drawRow(word, ans):
    if word == "":
        return ("\n|       |       |       |       |       |"
                "\n+-------+-------+-------+-------+-------+")
    else:
        word = word.upper()
        return (f"\n| {checkRight(word, ans, 0)[0]} {word[0]} {checkRight(word, ans, 0)[1]} "
                f"| {checkRight(word, ans, 1)[0]} {word[1]} {checkRight(word, ans, 1)[1]} "
                f"| {checkRight(word, ans, 2)[0]} {word[2]} {checkRight(word, ans, 2)[1]} "
                f"| {checkRight(word, ans, 3)[0]} {word[3]} {checkRight(word, ans, 3)[1]} "
                f"| {checkRight(word, ans, 4)[0]} {word[4]} {checkRight(word, ans, 4)[1]} |"
                "\n+-------+-------+-------+-------+-------+")


# noinspection PyDefaultArgument
def drawBoard(ans, words=[""]*6):
    board = "+-------+-------+-------+-------+-------+"

    for i, word in enumerate(words):
        board += drawRow(word, ans)

    return board


def printError(msg):
    print("!!! ERROR:" + msg.upper() + " !!!")
    sleep(1.5)


def gameEnd(ans, word, t):
    if word == ans:
        msg = "*** YOU WON ***\n"
    else:
        msg = "--- YOU LOST ---\n"

    msg += f"Turns taken: {t}/6"

    print(msg)
    if debug: printDebug(f"Correct answer was {answer.upper()}")
    input("\nPress Enter to play again . . . ")


def printLtrs():
    msg = ""
    for ltr in ascii_uppercase:
        msg += ["  ", "X ", "~ ", "* "][ltrs[ltr]]

    msg += "\n" + " ".join(ascii_uppercase)
    print(msg)


def printDebug(msg, pause=-1):
    print("### DEBUG: " + msg + " ###")
    if pause == 0:
        input("\nPress Enter to continue . . . ")
    elif pause > 0:
        sleep(pause)


def printHelp(cheats):
    msg = (
        "### HELP MENU ###\n"
        "[Commands]\n"
        "quit    - Quits the whole game\n"
        "restart - Restarts the game (and chooses a new word)\n"
        "cheats  - Activates debug mode"
    )
    
    if cheats:
        msg += (
            "\n\n"
            "[Debug Commands]\n"
            "ans     - Returns the answer to the current puzzle\n"
            "used    - Returns a list of the past 20 used words (most recent last)"
        )

    print(msg)
    input("\nPress Enter to continue . . . ")


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
        print(drawBoard(answer, wordList))
        printLtrs()
        inp = input("> ")

        ### Commands ###
        # Checking help menu PLACEHOLDER
        if inp.lower() == "help":
            printHelp(debug)
        # Quitting game
        elif inp.lower() == "quit":
            playing = False
            running = False
            break
        # Restarting game
        elif inp.lower() == "restart":
            playing = False
            break
        ### Debug
        elif inp.lower() == "cheats":
            debug = not debug
            printDebug(f"Debug is now {['OFF', 'ON'][debug]}")
        elif debug and (inp.lower() == "ans"):
            printDebug(f"Answer is: {answer.upper()}", 0)
        elif debug and (inp.lower() == "used"):
            printDebug(f"Words used are: {used}")
        ### Wrong input checks ###
        elif len(inp) != 5:
            printError("Input not of length 5")
        elif not inp.isalpha():
            printError("Input must be letters only")
        ### Correct user input ###
        else:
            wordList[turn] = inp
            turn += 1

            # Checking if game is over
            if (turn > 5) or (inp == answer):
                print(drawBoard(answer, wordList))
                gameEnd(answer, inp, turn)

                playing = False
                break

    # Picking next word
    answer, used = pickWord(used)
