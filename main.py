import random
import wordList
import validList

class colorCodes:
    NONE = ""
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    ENDC = "\033[0m"

def findOccurrences(str, ch):
    return [i for i, letter in enumerate(str) if letter == ch]

def printGameBoard(guesses, colorMap):
    for row in range(len(guesses)):
        for letter in range(5):
            print(colorMap[row][letter] + guesses[row][letter] + colorCodes.ENDC, end=" ")
        print()

def appendStats(gameWord, guesses, solved):
    statFile = open("stats.txt", "a")
    if solved:
        statFile.write("You solved " + gameWord + " in " + str(len(guesses)) + " guesses\n")
    else:
        statFile.write("You did not solve " + gameWord + "\n")
    for word in guesses:
        statFile.write(word + "\n")
    statFile.write("\n")
    statFile.close()

def main():
    gameWord = random.choice(wordList.fiveLetterWords)
    solved = False
    guesses = []
    colorStore = []
    colorMap = [["","","","",""], ["","","","",""], ["","","","",""], ["","","","",""], ["","","","",""], ["","","","",""]]
    count = 0

    while count < 6:
        val = input("Enter a 5 Letter Word: ").lower()
        if val in guesses:
            print("Already Guessed")
            continue
        elif (val not in validList.validGuesses) and (val not in wordList.fiveLetterWords):
            print("Not Valid")
            continue
        else:
            guesses.append(val)
            letters = [char for char in val]

            for letter in letters:
                if letter in gameWord:
                    occList = findOccurrences(gameWord, letter)
                    for occ in occList:
                        if gameWord[occ] == val[occ]:
                            colorMap[count][occ] = colorCodes.GREEN
                        else:
                            colorMap[count][val.find(letter)] = colorCodes.YELLOW

            printGameBoard(guesses, colorMap)
            count += 1

            if val == gameWord:
                print("Correct!")
                solved = True
                break


    if not solved:
        print("The correct word was:", gameWord)
    
    appendStats(gameWord, guesses, solved)

if __name__ == '__main__':
    main()