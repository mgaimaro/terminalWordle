# terminalWordle
Play the game Wordle in your Bash terminal

# How to run
In the terminalWordle directory, type python3 main.py

# Rules
1. A random 5-letter word will be selected as the hidden word
2. A player will make a maximum of 5 guesses to find the hidden word
3. If a letter appears in GREEN, the guessed letter is in the hidden word and in the correct position
4. If a letter appears in YELLOW, the guessed letter is in the hidden word but in the wrong position
5. A guess is considered invalid if it has already been guess or is not in the valid word list

# Stat Tracking
After each game, a file called stat.txt will be populated with your game data.

# Example Game
![image](https://user-images.githubusercontent.com/60477601/151012853-697a4de8-0b26-48e7-ba8d-cd08437d0eee.png)
