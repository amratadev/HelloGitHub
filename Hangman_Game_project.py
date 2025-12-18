import random
import hangman_stages
word_list=["Apple","Nice","beautiful","potato"]
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
lives = len(chosen_word)
game_over=False
while not game_over:
   guessed_letter=input("Guess a letter:").lower()
   for position in range(len(chosen_word)):
       letter=chosen_word[position]
       if letter==guessed_letter:
          display[position]=guessed_letter
   print(display)
   if guessed_letter not in chosen_word:
      lives-=1
      if lives == 0:
         game_over = True
         print("You lose")
      if '_' not in display:
         game_over=True
         print("You win")
      print(hangman_stages.stages[lives])
     

