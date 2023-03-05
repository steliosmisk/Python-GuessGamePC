import random

print("--WELCOME TO GUESSING GAME--")
print("[1] Start The Game")
print("[2] Exit")


ai_attempts = 10
user_choice = input("Enter (1/2): ")
while user_choice == '1' and user_choice != '2':
    try:
        # User Choose a number
        user_number = int(input("Enter a number from 1 to 100: "))
        # AI trying to guess
        ai = print("I think your number is:", random.randint(0, 100), "correct?")
        user_check = input("Type if its correct: (Y/N): ").lower()
        ai_ask = input("is lower or higher?: ").lower()
        while user_check == 'n' and ai_attempts > 0:
            if ai_ask == 'lower':
                ai = print("I think your number is:", random.randint(0, user_number), "correct?")
            else:
                ai = print("I think your number is:", random.randint(user_number, 100), "correct?")
            ai_attempts -= 1
            user_check = input("Type if its correct: (Y/N): ").lower()
            if user_check == 'y':
                print("HAHA I found your number!")
            elif ai_attempts == 0:
                ai_lost = input("I Lost can you tell me the number you chose?: ")
                print("Oh Ok! Have a nice day! Thanks for playing my game!")
        break

    except ValueError:
        print("Enter a number not a string!")
