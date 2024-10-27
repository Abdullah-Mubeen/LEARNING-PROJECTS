 

name = input("Enter your name: ")

print(f"Hello {name}, Welcome to the Game")

direction = input("You are in an abundant home. Where do you want to go? (left/right) ").lower()

if direction == 'left':
   killer = input("There is a killer (fight/run)").lower()
   if killer == "fight":
    print("You fight with courages and saved your life")
   elif killer == "run":
    print("You run and save your life")
elif direction == 'right':
  print("there you find what you want in the house")