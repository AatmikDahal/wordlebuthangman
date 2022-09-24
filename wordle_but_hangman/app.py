import time
import random
import game_stage

with open("words.txt", 'r') as file:
    file_data = file.readlines()
    word = random.choice(file_data).strip()


game_board = ["_"]*len(word)
print("Game Board -> ", game_board)




def main():
    wrong_attempts = 0
    user_input = input("Do you wish to start the game (Y|N): ")
    while user_input != "n":
        user_prompt = input("Guess the letter: ")
        
        if user_prompt in word:
            charIndex = word.index(user_prompt)
            game_board[charIndex] = user_prompt
            print("\nGuessed it right")
            print(game_board)
            
            if game_board == list(word):
                print(f"\nGuessed the word with {wrong_attempts} wrong attempts")
                print("\n YOU WON")
                ask = input("\n\nDo you want to play again(Y|N): ")
                if ask == 'y':
                    user_input = 'y'
                else:
                    user_input = 'n'
                
            
        elif user_prompt not in word:
            wrong_attempts += 1
            print("Guessed it wrong")
            
            if wrong_attempts == 1:
                print(game_stage.counter1)
                print("4 guesses left")
            elif wrong_attempts == 2:
                print(game_stage.counter2)
                print("3 guesses left")
            elif wrong_attempts == 3:
                print(game_stage.counter3)
                print('2 guesses left')
            elif wrong_attempts == 4:
                print(game_stage.counter4)
                print("1 guess left")
            elif wrong_attempts == 5:
                print(game_stage.counter5)
                print("You are out of chances")
                print("\n YOU LOST")
                print(f"The word was {word.upper()}")
                user_input='n'
                


print("Welcome to Wordle but Hangman w/o GUI")        
time.sleep(2)
main()

time.sleep(1)
print("Program Quit")

#can't detect the same letter in a word like L in calling 

