import random

# dice_rolling_game
# Loop
while True:
# 1. Ask: Roll the dice?
  user_input = input("Roll the dice? (y/n): ").lower()
# 2. If user enters y if user_input == 'y':
  if user_input == 'y':
  # 3.Generate two random numbers
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
  # 4. Print them
    print(f'({die1}, {die2})')
  # 5.If user enters n
  elif user_input =='n':
  # 6.Print thank you message
    print("Thank you for playing!")
  # 7.Terminate
    break
  # 8.Else
  else:
  # 9.Print invalid answer
    print("Invalid choice!")






    


