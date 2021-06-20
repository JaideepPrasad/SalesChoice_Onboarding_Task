# only move top most disk - good

#fuc - good
# move disk from source peg to destination peg
# all user defined

# system up date msgs
    # move completed - good
    # move invalid - good
    # game solved - good
    
#func
# display disk(s) in peg
# user defined

# current disk(s) in current pegs
A = ["red", "green", "purple", "blue"]
B = []
C = [] 

# disk size
disk_size = {
             "blue": 1,
             "purple": 2,
             "green": 3,
             "red": 4
            }

# ref_sol is reference solution, which will be used to compare with C to check if game is complete
ref_sol = ["red", "green", "purple", "blue"]

# the disks that are in game
local_disks = ["red", "green", "purple", "blue"]

# the pegs that are in the game
pegs = ["A", "B", "C"]

# will display all disk(s) in user defined peg
def display_peg():
    
    print("\n~~~~~~~~~~~~~~~~")
    print("| Current pegs |")
    print("| A            |")
    print("| B            |")
    print("| C            |")
    print("~~~~~~~~~~~~~~~~\n")
    
    display_peg = input("Which peg would you like to display?\n")
    
    if display_peg == "A":
        print(A)
    elif display_peg == "B":
        print(B)
    elif display_peg == "C":
        print(C)
    else:
        print("\nThat peg does not exist.")

# moved disk from one peg to another peg
def move_disk():
    
    disk = input("What disk would you like to move?\n")
    source_peg = input("Which peg is the disk located in?\n")
    destination_peg = input("Which peg do you want to move the disk?\n")
        
    # verify if disk is in game
    if disk in local_disks:
        pass
    else:
        print("Invalid disk,  please choose a valid disk.")
        
    # verify if source peg is in game
    if source_peg == "A":
        source_peg = A
    elif source_peg == "B":
        source_peg = B
    elif source_peg == "C":
        source_peg = C
    else:
        print("\nSource peg does not exist, please select another peg.")
        
    # verify if destination peg is in game
    if destination_peg == "A":
        destination_peg = A
    elif destination_peg == "B":
        destination_peg = B
    elif destination_peg == "C":
        destination_peg = C
    else:
        print("\nDestination peg does not exist, please select another peg.")
    
    # if user choice is valid
    if disk in source_peg:
        # check if disk in destination peg is bigger that disk we want to move
        if len(destination_peg) == 0 or disk_size[disk] < disk_size[destination_peg[-1]]:
            # move the disk from source peg to destination peg if disk is to top most disk in source peg
            if disk == source_peg[-1]:
                source_peg.pop()
                destination_peg.append(disk)
                print("\nmove complete")
            else:
                print("\nThere is another disk on top of the disk you want to move.")
        else:
            print("\nYou cannot place a bigger disk on top of a smaller disk.")
    else:
        print("\nDisk is not in peg.")  

# help fuction with explination/documnetation
def help_func():
    
    print("\nWelcome to the tower of Hanio, Please enter the number of the corresponding option from the menu.")
    print("\nMove the disks from one peg to another.")
    print("\nThe object is to stack disks red, green, purple and blue on to peg C in that order.")
    print("\nThe only rule is that you can only move a disk if that disk is the top most disk in the peg and that you cannot place a bigger disk on a smaller disk.")

# menu loop
while True:
         
    # check if game is complete
    if C == ref_sol:
        print("Congradz on completing the game :D")
        break
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("| Please choose an option |")
    print("| 1. Move Disk            |")
    print("| 2. Display Peg          |")
    print("| 3. Help                 |")
    print("| 4. Exit                 |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    # get user input
    user_input = input("Pick a number: \n") # what if user puts char 
    user_input = int(user_input)
    
    if user_input == 1:
        move_disk()
    
    elif user_input == 2:
        display_peg()
        
    elif user_input == 3:
        help_func()
    
    elif user_input == 4:
        break
    
    else:
        print("\nInvalid response, please choose from the options provided.")