import os
import random

def answers():
  i = random.randint(0, 2315)
  with open('allwords.txt') as x:
    arr = x.readlines()
    save = arr[i]
    word = save[0] + save[1] + save[2] + save[3] + save[4]
    return word
  
def search(guess):
  with open('allwords.txt') as x:
    arr = x.readlines()
    for i in arr:
      i = i[0] + i[1] + i[2] + i[3] + i[4]
      if str(guess) == str(i):
        return False
    return True
  
def playGame(word):
  Keyboard = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  i = 1
  save = ""
  while i != 7:
    guess = input("guess:")
    if search(guess):
      print("That word is not on the possible words list!")
      continue
    os.system('cls||clear')
    showColors = colors(word, guess)
    visual = showColors[0] + "|"+showColors[1] + "|"+showColors[2] + "|"+showColors[3] + "|" + showColors[4]
    save += "\n" + visual  
    print (save)
    for j in range(6-i):
      print(" | | | | ")
    if guess == word:
      print ("Congratulations! The word was " + word + "! It took you " + str(i) + " tries!")
      break
    i += 1
    print("\n")
    Keyboard = keyboard(Keyboard, colors(word, guess))[0]
    print(keyboard(Keyboard, colors(word, guess))[1])
  if i == 7:
    print("Oh no! You weren't able to guess the word! The word was " + word)

def colors(x, y):
  answer = []
  color = []
  for i in range(5):
    answer.append(x[i])
  guess = []
  for i in range(5):
    guess.append(y[i])
  for j in range(len(guess)):
    for i in range(len(answer)):
      if guess[j] == answer[i]:
        if guess[j] == answer[j]:
          color.append("\x1b[;32m" + guess[j] + "\x1b[1;37m")
          answer[j] = "1"
          guess[j] = "0" 
        elif guess[i] == answer[i]:
          color.append("\x1b[1;32m" + guess[i] + "\x1b[1;37m")
          answer[i] = "1"
          guess[i] = "0" 
        else:
          color.append("\x1b[1;33m" + guess[j] + "\x1b[1;37m")
          answer[i] = "1"
          guess[j] = "0"
        break
  for l in range(len(guess)):
    if guess[l] != "0":
      color.insert(l, "\x1b[1;90m" + guess[l] + "\x1b[1;37m")
  return color

def keyboard(keyboard, colors):
  for i in colors:
    prints = ""
    letter = i[-8]
    color = i[-11] + i[-10]
    for j in range(len(keyboard)):
      if keyboard[j] == letter:
        if color == "32":
          keyboard[j] = i
        elif color == "33":
          keyboard[j] = i
        elif color == "90":
          keyboard[j] = i
  for i in keyboard:
    prints += i + " "
  return keyboard, prints

def gamemodes():
  print("Welcome to my wordle! There are currently 2 gamemodes: \nRandom: a computer chooses the word for you \nTwo Player: another player chooses the word for you")
  while True:
    print("\nPlease type 'r' if you want to play 'Random'")
    print("Please type '2' if you want to play 'Two Player'")
    x = input("Please type 'rules' if you want to read the rules and credit: ")
    if x == "r":
      word = answers()
      print ("Random selected!\n")
      break
    if x == "2":
      while True:
        word = input("Please input a five letter word: ")
        if search(word):
          print("Guess is not on possible words list")
          continue
        break
      print ("\n")
      os.system('cls||clear')
      break
    if x == "rules":
      print("Guess the WORDLE in six tries. \nEach guess must be a valid five-letter word. Hit the enter button to submit. \nAfter each guess, the color of the tiles will change to show how close your guess was to the word. \nFull credit to idea and rules goes to New York Times's Wordle game, only the code is mine.")
      continue
    else:
      continue
  return word
      
playGame(gamemodes())

