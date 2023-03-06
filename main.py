import random
import os
import numpy as np

class UserOption():
    def __init__(self, name, fnHandle):
        self.name = name
        self.fnHandle = fnHandle

class Player():
    def __init__(self, name):
        self.name = name
        self.wordList = []

    def __str__(self):
        return "{} ({} words)".format(self.name, len(self.wordList))

    def addWord(self, newWord):
        self.wordList.append(newWord)

    def removeWord(self, wordToRemove):
        try:
            idxOfWord = self.wordList.index(wordToRemove)
            del self.wordList[idxOfWord]
        except:
            return

    def getRandomWord(self):
        numWords = len(self.wordList)
        if numWords > 0:
            wordIdx = random.randrange(numWords)
            return self.wordList[wordIdx]
        else:
            raise Exception("{} has no words".format(self.name))



class GameState():

    def __init__(self):
        self.players = []
        self.wordLists = []
        self.defaultWordList = []
        
    def addPlayer(self, newPlayerName):
        if self.playerExists(newPlayerName):
            raise Exception("Player already exists in list")

        newPlayer = Player(newPlayerName)
        self.players.append(newPlayer)
        
    def removePlayer(self, playerName):
        for idx, thisPlayer in enumerate(self.players):
            if thisPlayer.name == playerName:
                del self.players[idx]

    def getPlayerByName(self, playerName):

        for thisPlayer in self.players:
            if thisPlayer.name == playerName:
                return thisPlayer
        return []
        
    def playerExists(self, playerName):

        for thisPlayer in self.players:
            if thisPlayer.name == playerName:
                return 1

        return 0

    def getNumPlayers(self):
        return len(self.players)

    def getRandomPlayer(self):
        return self.players[random.randrange(self.getNumPlayers())]

    def getRandomPlayerWithWordsExcludingOne(self, nameExcluded):

        if self.checkAnyPlayersHaveWords() == 0:
            raise Exception("No players have available words")

        eligiblePlayersWithWords = []
        for player in self.players:
            if player.name == nameExcluded:
                continue
            if len(player.wordList) > 0:
                eligiblePlayersWithWords.append(player)

        randEligiblePlayer = eligiblePlayersWithWords[random.randrange(len(eligiblePlayersWithWords))]

        return randEligiblePlayer


    def addWordForPlayer(self, playerName, newWord):
        if self.playerExists(playerName):
            player = self.getPlayerByName(playerName)
            player.addWord(newWord)

    def removeWordFromPlayer(self, playerName, removeWord):
        if self.playerExists(playerName):
            player = self.getPlayerByName(playerName)
            player.removeWord(removeWord)

    def checkAllPlayersHaveWords(self):
        for player in self.players:
            if len(player.wordList) == 0:
                return 0

        return 1

    def checkAnyPlayersHaveWords(self):
        for player in self.players:
            if len(player.wordList) > 0:
                return 1
        return 0

    def getNumPlayersWithWords(self):
        numPlayersWithWords = 0
        for player in self.players:
            if len(player.wordList) > 0:
                numPlayersWithWords += 1
        return numPlayersWithWords

    def clearPlayers(self):
        self.players = []


            

def clearScreen():
    clear = lambda: os.system('cls')
    clear()


def addPlayer(gameState):

    playerName = input("Enter player name (or type 'done' when all players are added): ")
    if playerName == "done":
        return

    if gameState.playerExists(playerName):
        input("The name {} is already taken. Hit [Enter] to continue".format(playerName))
        return

    gameState.addPlayer(playerName)

    thisWord = "temp"
    while thisWord != "done":
        thisWord = input("Enter a word for others to guess, or type 'done' when you're done: ")
        if thisWord == "done":
            break
        gameState.addWordForPlayer(playerName, thisWord)
        print(thisWord + " added. You have " + str(len(gameState.getPlayerByName(playerName).wordList)) + " words.\n")

    clearScreen()

def removePlayer(gameState):

    playerNameToRemove = input("Remove which player?: ")
    
    if gameState.playerExists(playerNameToRemove):
        gameState.removePlayer(playerNameToRemove)
    else:
        print("\nNo player named {} to remove".format(playerNameToRemove))  

def clearPlayers(gameState):
    print("You've selected 'clear players'. This will erase all players and word lists")
    confirm = input("Are you sure? Type y and [Enter] to confirm: ")
    if (confirm == "y") | (confirm == "yes"):
        gameState.clearPlayers()


def addWordsForPlayer(gameState):

    playerToAddWordsFor = input("Add words for which player?: ")
    
    if gameState.playerExists(playerToAddWordsFor):
        newWord = "temp"
        while newWord != "done":
            newWord = input("Enter a word for others to guess, or type 'done' when you're done: ")
            if newWord == "done":
                return
            gameState.addWordForPlayer(playerToAddWordsFor, newWord)
            print(newWord + " added. You have " + str(len(gameState.getPlayerByName(playerToAddWordsFor).wordList)) + " words.\n")
    else:
        input("{} is not a current player. Hit [Enter] to continue\n".format(playerToAddWordsFor))

    
def printPlayersAndWordCounts(gameState):
    numPlayers = len(gameState.players)
    
    if numPlayers == 0:
        print("\nNo current players\n")
    else:
        print("\n")
        for i in range(numPlayers):
            print("{}:\t{} words available".format(gameState.players[i].name, len(gameState.players[i].wordList)))
        print("\n")


def showPlayerWord(theWord):
    print("\nThe word is: " + theWord)
    input("\nOnce you've got it memorized, hit [enter]")
    clearScreen()


def dontShowPlayerWord():
    print("\n\nYou don't get to see the word!\n")
    input("feel sad, and then hit [enter]")
    clearScreen()


def playRound(gameState):

    clearScreen()

    if gameState.getNumPlayersWithWords() <= 1:
        input("One or fewer players have words to pick, need other players to enter words. Hit [Enter] to return to the menu")
        return

    if gameState.checkAllPlayersHaveWords() == 0:
        playerInput = input("some players don't have words. Hit [Enter] to play anyway, or type 'menu' to go back to menu: ")
        if playerInput == "menu":
            return

    playerLeftOut = gameState.getRandomPlayer()

    playerToPickWordFrom = gameState.getRandomPlayerWithWordsExcludingOne(playerLeftOut.name)

    secretWord = playerToPickWordFrom.getRandomWord()

    for player in gameState.players:
        print("\nShow computer to " + player.name)
        input("hit enter when ready")
        if player.name != playerLeftOut.name:
            showPlayerWord(secretWord)
        else:
            dontShowPlayerWord()

    print("\neveryone has seen word, ready to play!\n")
    playerToPickWordFrom.removeWord(secretWord)


def setupTest():

    gameState = GameState()

    p1 = Player("andy")
    p1.wordList = ["moose", "pig", "manbearpig"]

    p2 = Player("joe")
    p2.wordList = ["jello", "pizza", "meat", "banana"]

    p3 = Player("neil")
    p3.wordList = ["hacking", "tuna", "fateful findings", "the most secret government secrets"]

    gameState.players = [p1, p2, p3]
    return gameState


def runTest():
    gameState = setupTest()
    playRound(gameState)


    
def main():
    random.seed()

    gameState = GameState()
    
    optionList = []
    optionList.append(UserOption("add player", lambda gameState: addPlayer(gameState)))
    optionList.append(UserOption("remove player", lambda gameState: removePlayer(gameState)))
    optionList.append(UserOption("add words for player", lambda gameState: addWordsForPlayer(gameState)))
    optionList.append(UserOption("clear players", lambda gameState: clearPlayers(gameState)))
    optionList.append(UserOption("play round", lambda gameState: playRound(gameState)))    
    optionList.append(UserOption("exit", lambda gameState: print("exiting...")))
    
    
    numOptions = len(optionList)
    selectedOptionName = ""
    
    while selectedOptionName != "exit":
        clearScreen()
        printPlayersAndWordCounts(gameState)

        userPrompt = "Select Option: \n"
        for idx, userOption in enumerate(optionList):
            userPrompt = userPrompt + "  {}: {}\n".format(idx + 1, userOption.name)
        
        validOption = 1
        try:
            typedOption = input(userPrompt)
            optionIdx = int(typedOption) - 1
            if int(typedOption) > (numOptions):
                validOption = 0
        except:
            validOption = 0
            
        if validOption:
            selectedOption = optionList[optionIdx]
            selectedOptionName = selectedOption.name
            selectedOption.fnHandle(gameState)
        else:
            print("{} is an invalid option".format(typedOption))


main()