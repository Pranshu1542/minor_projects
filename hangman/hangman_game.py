import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "banana", "cherry", "date", "elderberry"]

Lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

length_of_word = len(chosen_word)
for letter in range(length_of_word):
	placeholder += "_"
print(placeholder)

game_over = False
correct_word = []
while not game_over:
	guess = input("Guess a letter : ").lower()
	display = ""

	for letter in chosen_word:
		if letter == guess:
			display += letter
			correct_word.append(letter)
		elif letter in correct_word:
			display += letter
		else:
			display += "_"

	print(display)
	
    
	if guess not in chosen_word:
		Lives -= 1
		if Lives == 0:
			game_over = True
			print("You Lose!")


	if "_" not in display:
		game_over = True
		print("You Win!")	
		
	print(stages[Lives])
