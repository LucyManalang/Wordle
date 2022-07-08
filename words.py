import random

class words():

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
  
      