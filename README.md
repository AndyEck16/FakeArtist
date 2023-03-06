# FakeArtist
Terminal Based Controller to support playing Fake Artist Goes To New York Game

Python script to support playing rounds of Fake Artist Goes To New York

## Dependencies
Ran and tested on Python 3.8.13 using Anaconda3
Numpy version 1.22.3

## Game Overview
The premise of the game is that all players except for one (the Fake Artist) are given a secret prompt to draw.
All players collaborate on the same picture and word, even the player who is not given the prompt.
One at a time, players make a new contiunous line on the drawing.
After two lines are drawn, all players vote on who they think wasn't given the word at the beginning.
If the player who got the most votes is indeed the Fake Artist who didn't know the word, that player gets to guess on what the secret prompt is that the rest of the players were given.
If the group votes for the wrong player, or if the Fake Artist correctly guesses the prompt (or gets close enough), the fake artist wins.

## What this tool does
* Controls adding and removing players from the game
* Allows each player to add words to a list that other players cannot see
* Play one round of fake artist which involves:
  * Secretly choosing one of the players to be the fake artist
  * Picking a secret prompt that is _not_ from that players list to be the secret word
  * Showing the word to all players except for the fake artist, who will instead see a message telling them they don't get to see the word


## Directions on how to use
Open a cmd terminal using either anaconda cmd.exe, or normal cmd terminal if you have numpy installed with your python
Run program main.py using an Anaconda cmd.exe prompt, or python prompt if you have numpy set up on it.
(You can also run this in PyCharm using the debugger, but the screen won't get cleared properly to hide words from other players. Get around this by resizing the output pane to be very short)

Text based menu will pop up with various options for running the game. Type the number of the option you want to run and then hit enter.
Options are:
1. add player
   - Prompts to type the name of the new player you are adding
   - Prompts player to enter secret words or prompts that could be chosen. Player enters one word at a time by typing it and hitting "enter". When they are done, they type 'done' and the screen will return to the main menu
2. remove player
   - Prompts to type the name of a player you want to remove from the game. Currently is case-sensitive. If the typed name doesn't match a current player, nothing happens.
3. add words for player
   - Type the name of an existing player. The player can then come to the terminal and add words to their current list
4. clear players
   - Clears all players and word lists and returns game state to what it is on startup
5. play round
   - Runs a single round of the game
     - For each player, displays text "show computer to [player], hit enter when ready"
     - After hitting enter, that player will either see a secret word, or see a message that tells them they don't get to know the word
     - Player then hits enter to clear the text and move onto the next player
     - after all players have had a chance at the terminal, you can play the game! The terminal will return to showing the main menu, as well as a player list and how many words each player has remaining in their list
 6. exit
    - exits the program



