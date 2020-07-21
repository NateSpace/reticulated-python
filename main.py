print("welcome to the guessing game please pick a number 1 to 10 and I will try to guess it")

guess = 5
correct = False
minimum = 1
maximum = 10
while not correct:
  print(f"my guess is {guess}. ")
  answer = input("am I A) correct B) too high or C) too low:")
  if answer == "a":
    print("I guessed It!")
    correct = True
  elif answer == "b":
    maximum = guess
    guess = (minimum + guess) // 2
  elif answer == "c":
    minimum = guess 
    guess = round ((maximum + guess) / 2)