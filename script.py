from stack import Stack

linebreak = "---------------------"
print("\nLet's play Towers of Hanoi!!\n" + linebreak*2)

#Create the Stacks
stacks =[]
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n" + linebreak*2 + "\n"))

while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

for i in range(num_disks,0,-1):
  left_stack.push(i)

# Test starting stack value
#print(left_stack.print_items())
#print(middle_stack.print_items())
#print(right_stack.print_items())

num_optimal_moves = (2**num_disks)-1
print("\nThe fastest you can solve this game is in {num} moves\n".format(num=num_optimal_moves) + linebreak*2)

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    #Present the user with a description of their choice e.g Enter L for left, or Enter M for Middle.
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(letter=letter, name=name))
    user_input = input("")
    # Allow user to input a choice for the input. Input must be in capitals.
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
    else:
      print(linebreak+"Invalid Stack Name"+linebreak)

#Play the Game

num_user_moves = 0

# Main Loop controlling the game. For game to end right stack must have the total number of disks.

while right_stack.get_size() != num_disks:
  # The user needs to see the stacks after each move, to determine the next move.
  print(linebreak + "\n..Current Stacks..." )
  for stack in stacks:
    stack.print_items()
  print(linebreak)
  # This is where we allow the user to move the rings on the stacks.
  while True:
    # The user can now define the move.
    print("\nWhich stack do you want to move from?\n" + linebreak*2)
    from_stack = get_input()
    if from_stack.get_size() == 0:
      print(linebreak + "\nThe chosen stack has no available rings!\n" + linebreak)
      break
    print("\nWhich stack do you want to move to?\n" + linebreak*2)
    to_stack = get_input()
    # The if statement below tests if the move is valid, first by checking if there are discs to move!
    if to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print(linebreak + "\nThe disc on the current stack is smaller\n" + linebreak)


print(linebreak*4 + "\nYou completed the game in {num} moves, and the optimal number of moves is {optimal}\n".format(num=num_user_moves, optimal=num_optimal_moves) + linebreak*4)