import random
rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''
paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''
scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''
game_images=[rock,paper,scissors]
user_choice=int(input("enter your choice(0 for rock,1 for paper,2 for scissors):"))

if user_choice >=3 or user_choice < 0:
  print("You entered invalid number,You lose")
else:
  print("user_choice:",user_choice)
  print(game_images[user_choice])
  
  computer_choice=random.randint(0,2)
  print("computer_choice:",computer_choice)
  print(game_images[computer_choice])
  
  

  if computer_choice==user_choice:
    print("It's a drawn")

  elif computer_choice==0 and user_choice==2:
   print("You Lose")  

  elif user_choice==0 and computer_choice==2:
   print("You Win")

  elif computer_choice > user_choice:
    print("You Lose.")

  elif user_choice>computer_choice:
   print("You Win")


