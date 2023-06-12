import random

def rps():
 the_list = ['rock','paper','scissors']

 z = random.choice(the_list)
 x = input('Pick one: Rock, Paper or Scissors?  ').lower()
 print('me: '+x)
 print('computer: '+z)

 while z == 'rock':
      if x == 'rock':
          print('a draw')
      elif x == 'paper':
          print('You win')
      elif x == 'scissors':
          print('you lose')
      break


 while z == 'paper':
      if x == 'rock':
          print('You lose')
      elif x == 'paper':
          print('You draw')
      elif x == 'scissors':
          print('you win')
      break
 while z == 'scissors':
      if x == 'rock':
          print('you win')
      elif x == 'paper':
          print('You lose')
      elif x == 'scissors':
          print('you draw')
      break



def again():
    a = input('Would you play again?(yes/no) ')
    if a == 'yes':
        return a
    else:
      print('good day buddy ')



rps()
while again():
    rps()

