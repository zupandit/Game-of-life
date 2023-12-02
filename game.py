# Name: Zaid Nissar
# UCID: 30198174
# Tutorial: 10

# Version 1.0: Functions that gave the co-ordinates of Empty Points and co-ordinates of Cripper Points were added.
# Version 2.0: Function that returned a world after only births was created. A function to deepcopy 2d lists
# was added. A function that returned a world after only deaths was created.
# Version 3.0: A function that merges two worlds together (after birth and after world) to give out a final world
# was added.
# Version 4.0: Logic was improved upon. Hard coded worlds by Dr Tam were added and tested. A function that asks the
# user for initial starting world was added.
# Version 5.0: Display function was defined and made dynamic so any rectangular 2d list could be used.
# Version 6.0: a file read function that converts a txt file into a 2d list was made. A 7th option was added to
# the bioSphereStarter() function.
# Version 7.0: Error Handling was implemented at every user interaction point. Error handling for files was added too.
# Version 8.0: Program was polished and documentation was added.

# Program Summary: All the functional requirements work.
# 1) All the hard-coded initial biospheres cases give the correct new biosphere after each turn. Works on all six!
# 2) Debug Mode has been implemented.
# 3) Program does run until user chooses to quit.
# 4) User has the option to import the initial biosphere from a txt file-> he is prompted for entering file name after
#    entering 7.
# 5) All the functions work for any rectangular 2d lists.
# 6) Read function is able to convert not only perfect size txt files into 2d lists but any arbitrarily sized
# rectangular file into 2d lists.
# 7) Error handling has been implemented in all cases including file reading cases where if there is an error then the
#    user is re-prompted.
# 8) Display function works perfectly.
# 9) Main loop runs until the user quits.

# IMPORTANT!!!
# NOTE: The reader() function works only when a newline(\n) is present after the end of the world in the .txt file
# that is after the cell -> world[lastRow][lastColumn]. The next line should be empty!!

# Defining Global Constants:
END_OF_LINE = ""
EMPTY = ""
NEWLINE = "\n"
SPACE = " "
CRITTER = '*'
NO_LIFE = ' '


# @Args(none)
# The function asks the user to choose the starting world. A user can either choose a world hard-coded by Dr. Tam or
# choose to input a txt file.
# @returns (Str -> user selection)
def bioSphereStarter():
    print('Choices for starting biospheres:')
    print('(1) Empty')
    print('(2) Single critter')
    print('(3) Single birth')
    print('(4) Simple birth')
    print('(5) Edgey testing')
    print('(6) It\'s a complex world')
    print('(7) Get from your own custom file')

    # Error Handling has been implemented:
    correctInput = False
    while not correctInput:
        try:
            user_input = int(input('Selection: '))
            correctInput = True
        except ValueError:
            print('Please enter the correct option: ')

    return user_input


# Game of Life simulation
# Author:  James Tam
# Version: June 6, 2020.
# The functions from oneEmpty() to sixthComplexCases() have been authored by Dr. Tam and have been used under his
# directions and approval.
# Note: Max_Rows and Max-Columns have been added to them which are essential for the well functioning of the rest of
# program.
# @args(none)
# Functions return a hard-coded starting point for the game of life.
# Return (a 2d list -> a starting world/biosphere,(int)-> No. of rows in the world, (int)-> no. of columns in the world.
def oneEmpty():
    world = []
    world = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    # Calculating no. of rows and columns:
    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


def twoSingleCritter():
    world = []
    world = [
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


def threeSingleBirth():
    world = []
    world = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "*", " ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


def fourthSimpleBirth():
    world = []
    world = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "*", "*", " ", " ", " ", " ", " ", " "],
        [" ", "*", " ", "*", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


def fifthCreateListEdgeCases():
    world = []
    world = [
        ["*", " ", "*", " ", " ", " ", " ", " ", " ", "*"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        [" ", " ", " ", " ", " ", " ", " ", " ", "*", " "],
        ["*", "*", " ", " ", " ", " ", " ", " ", " ", "*"]
    ]
    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


def sixthComplexCases():
    world = []
    world = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "*", " ", " ", " ", " ", " "],
        [" ", "*", " ", " ", " ", "*", " ", " ", " ", " "],
        [" ", " ", " ", "*", "*", "*", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


# @args(none)
# Function reads a txt file and converts it into a 2d list.
# NOTE: The txt file must be handled with care. Only txt files with a newline at the end of last world[row][column]
# with an empty line afterwards will work.
# @returns (a 2d list -> a world created from reading the txt file; (int) -> No. of rows; (int) No. of Columns)
def reader():
    fileOK = False
    world = []
    # Error handling implemented:
    while not fileOK:
        try:
            filename = input('File name: ')
            inputfile = open(filename, "r")
            fileOK = True
            aLine = inputfile.readline()
            if aLine == EMPTY:
                print('Empty file')
            else:
                currentRow = 0
                while aLine != END_OF_LINE:
                    # Appending new rows to world as each line is read in the txt file except for the very last
                    # EMPTY line where the function stops reading the file
                    world.append([])
                    currentCharacter = 0
                    while aLine[currentCharacter] != NEWLINE:
                        # Appending the characters:
                        world[currentRow].append(aLine[currentCharacter])
                        currentCharacter += 1
                    currentRow += 1
                    aLine = inputfile.readline()
                inputfile.close()
        except IOError:
            print('Problem reading from file')
            fileOK = False

    MAX_ROWS = len(world)
    MAX_COLUMNS = len(world[0])

    return world, MAX_ROWS, MAX_COLUMNS


# @args([a list] -> a list that needs to be copied)
# Function creates a deepcopy ( the best implementation I could do) of the source list).
# @return([a list]a copied version of the source list)
# In context to A3 the argument and return values both will be 2d lists
def copier(source):
    copy = [element[:] for element in source]
    return copy


# @args([2d list] -> starting world on which the rules of birth and death will be applied)
# Function returns the co-ordinates of empty potential birthplaces for crippers.
# @return([1d list] -> a list with co-ordinates of empty potential birthplaces for crippers)
def co_ordinate_getter_birth(original_world):
    coordinate_list = []
    for row in range(len(original_world)):
        for element in range(len(original_world[row])):
            if original_world[row][element] == NO_LIFE:
                # Stored as string but later converted to int. This is done so they are easy to store
                coordinate_list.append(str(row) + str(element))
    return coordinate_list


# @args(starting world on which the rules of birth and death will be applied)
# Function returns a list which has the co-ordinates of critters in the starting world which
# Will be further used in the program to
# determine if they will stay alive or dead for the next turn.
# @return(a list with co-ordinates of where crippers are in the starting world)
def co_ordinate_getter_critter(original_world):
    coordinate_list = []
    for row in range(len(original_world)):
        for element in range(len(original_world[row])):
            if original_world[row][element] == CRITTER:
                coordinate_list.append(str(row) + str(element))
    return coordinate_list


# @args((2d list) -> starting world on which the rules of birth will be applied,(int) -> No.
# of rows of starting world, (int) -> No. of columns of starting world)
# Function takes points from the co_ordinate_getter_birth() returned list. It checks the neighbors of each co-ordinate
# and counts the number of critters that surround it. After this it determines if a birth should happen or not and
# adequately returns a world with only new birth critters.
# @return((a 2d list) -> a world of only new birth critters)
def only_birth(original_world, MAX_ROWS, MAX_COLUMNS):
    # a deepcopy is created so original world is not disturbed:
    new_world = copier(original_world)
    # new deep copy is cleared to ready it for birth of new critters:
    for row in range(len(new_world)):
        for element in range(len(new_world[0])):
            new_world[row][element] = NO_LIFE
    # Keeping track of neighbouring critters:
    critter_count = 0
    # Getting points from initial world/biosphere:
    coordinate_list = co_ordinate_getter_birth(original_world)
    # Checking the neighbours of the points in the original list:
    for coordinates in coordinate_list:
        row = int(coordinates[0])
        column = int(coordinates[1])
        surroundingRow = row - 1
        while surroundingRow <= row + 1:
            surroundingColumn = column - 1
            while surroundingColumn <= column + 1:
                if 0 <= surroundingRow < MAX_ROWS and 0 <= surroundingColumn < MAX_COLUMNS:
                    if original_world[surroundingRow][surroundingColumn] == CRITTER:
                        critter_count += 1
                surroundingColumn += 1
            surroundingRow += 1
        # If critters = 3 then a new birth is added to the new world:
        if critter_count == 3:
            new_world[row][column] = CRITTER
        critter_count = 0
    birth_world = new_world
    return birth_world


# @args((2d list) -> starting world on which the rules of death will be applied,(int) -> No.
# of rows of starting world, (int) -> No. of columns of starting world)
# Function takes points from the co_ordinate_getter_critter() returned list. It checks the neighbors of each co-ordinate
# and counts the number of critters that surround it. After this it determines if a critter should stay alive or not
# and adequately returns a world with only alive critters from the original world (no newborn critters).
# @return ((2d list) -> a world of only surviving critters from the original world. No newborn critters.
def death_world(original_world, MAX_ROWS, MAX_COLUMNS):
    # a deepcopy is created so original world is not disturbed:
    new_world = copier(original_world)
    critter_count = 0
    # Getting points from initial world/biosphere:
    coordinate_list = co_ordinate_getter_critter(original_world)
    # Code that checks the neighbours:
    for coordinates in coordinate_list:
        row = int(coordinates[0])
        column = int(coordinates[1])
        surroundingRow = row - 1
        while surroundingRow <= row + 1:
            surroundingColumn = column - 1
            while surroundingColumn <= column + 1:
                if 0 <= surroundingRow < MAX_ROWS and 0 <= surroundingColumn < MAX_COLUMNS:
                    if original_world[surroundingRow][surroundingColumn] == CRITTER:
                        critter_count += 1
                surroundingColumn += 1
            surroundingRow += 1
        # (critter_count -1) because the code also traverses through the point itself so surrounding critters must be
        # total critters counted - 1 ( 1 being the critter whose neighbours we are checking itself)
        if (critter_count - 1 < 2) or (critter_count - 1 > 3):
            new_world[row][column] = ' '

        critter_count = 0
    death_world = new_world
    return death_world


# @Args((2d list) -> returned only Birth world from only_birth(); (2d list) -> returned only surviving critter world
# from death_world)
# Function merges the after death and the after birth worlds and returns to us the final world
# on which the games of birth and death have been fully implemented.
# @returns ((2d list) -> The final world )
def finalWorld(afterBirth_matrix, afterDeath_matrix):
    # Code that compares the two worlds and merges them:
    for row in range(len(afterBirth_matrix)):
        for element in range(len(afterBirth_matrix[0])):
            if afterBirth_matrix[row][element] != afterDeath_matrix[row][element]:
                # The critters that make it to the next turn:
                afterDeath_matrix[row][element] = '*'
    final_World = copier(afterDeath_matrix)
    return final_World


# @args((2d list) -> world whose points will be debugged/checked ,(int) -> No.
# of rows of the world, (int) -> No. of columns of the world)
# Function shows points and how many critters surround it. Helps us check the logic. Prints out important stuff.
# @returns(none)
def debugMode(world, MAX_ROWS, MAX_COLUMNS):
    empty_point_list = co_ordinate_getter_birth(world)
    critter_point_list = co_ordinate_getter_critter(world)

    print('Debugging Empty Points (potential birth places): ')
    star_count = 0
    for coordinates in empty_point_list:
        row = int(coordinates[0])
        column = int(coordinates[1])
        surroundingRow = row - 1
        while surroundingRow <= row + 1:
            surroundingColumn = column - 1
            while surroundingColumn <= column + 1:
                if 0 <= surroundingRow < MAX_ROWS and 0 <= surroundingColumn < MAX_COLUMNS:
                    if world[surroundingRow][surroundingColumn] == CRITTER:
                        star_count += 1
                surroundingColumn += 1
            surroundingRow += 1
        print('Co-ordinate: ', row, column, '\t', 'No. of surrounding Critters:', star_count)
        star_count = 0

    print('Debugging Active Critters:')
    for coordinates in critter_point_list:
        row = int(coordinates[0])
        column = int(coordinates[1])
        surroundingRow = row - 1
        while surroundingRow <= row + 1:
            surroundingColumn = column - 1
            while surroundingColumn <= column + 1:
                if 0 <= surroundingRow < MAX_ROWS and 0 <= surroundingColumn < MAX_COLUMNS:
                    if world[surroundingRow][surroundingColumn] == CRITTER:
                        star_count += 1
                surroundingColumn += 1
            surroundingRow += 1
        print('Co-ordinate: ', row, column, '\t', 'No. of surrounding Critters:', star_count)
        star_count = 0


# @args( (2d list) -> Initial biosphere/world on which the rules of birth and death shall be applied; (2d list) -> new
# biosphere/world on which the rules of the game have been applied; (int) -> No. of rows in the worlds (same for both
# initial and new); (int) => No. of columns in the worlds (same for both initial and new).
# Function displays the oldWorld on which rules of game were not applied and then displays a new world which is the
# old world on which the rules of the game HAVE been applied.
# @return(none)
# NOTE: The function is originally authored by Dr. Tam but as per his instructions it has been changed in such a way
# that any rectangular world can be displayed by it.
# Max_rows and Max_columns was added so the display function would be dynamic and be utilized by any rectangular
# 2d list.
def display(oldWorld, newWorld, MAX_ROWS, MAX_COLUMNS):
    # Displays a row at a time of each list

    print("BEFORE\t\t\t\t\tAFTER")
    for r in range(0, MAX_ROWS, 1):

        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range(0, MAX_COLUMNS, 1):
            print("%s" % " -", end="")
        print("#\t", end="")
        # (Dashes for new list)
        for i in range(0, MAX_COLUMNS, 1):
            print("%s" % " -", end="")
        print()

        # Display one row of old world list
        for c in range(0, MAX_COLUMNS, 1):
            # Display: A vertical bar and then element (old list)
            print("|%s" % (oldWorld[r][c]), end="")
        # Separate the lists with a number sign and a tab
        print("", end="#\t")

        # Display one row of new world list
        for c in range(0, MAX_COLUMNS, 1):
            # Display: A vertical bar and then element (new list)
            print("|%s" % (newWorld[r][c]), end="")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range(0, MAX_COLUMNS, 1):
        print("%s" % " -", end="")
    print("#\t", end="")

    # Row of dashes after end of each row (new world list)
    for i in range(0, MAX_COLUMNS, 1):
        print("%s" % " -", end="")
    print()


# @args(none)
# function keeps track of the state of the game including if the game has been quit or not. It does some error handling
# as well for user inputs.
# It has the call to most functions inside it.
# @returns(none)
def start():
    # Zero turns have been done at the start:
    turn = 0
    # Game is not over at start:
    game_over = False

    # Error checking has been implemented:
    correctValue = False
    while not correctValue:
        user_choice = bioSphereStarter()
        if user_choice == 1:
            original_world, MAX_ROWS, MAX_COLUMNS = oneEmpty()
            correctValue = True
        elif user_choice == 2:
            original_world, MAX_ROWS, MAX_COLUMNS = twoSingleCritter()
            correctValue = True
        elif user_choice == 3:
            original_world, MAX_ROWS, MAX_COLUMNS = threeSingleBirth()
            correctValue = True
        elif user_choice == 4:
            original_world, MAX_ROWS, MAX_COLUMNS = fourthSimpleBirth()
            correctValue = True
        elif user_choice == 5:
            original_world, MAX_ROWS, MAX_COLUMNS = fifthCreateListEdgeCases()
            correctValue = True
        elif user_choice == 6:
            original_world, MAX_ROWS, MAX_COLUMNS = sixthComplexCases()
            correctValue = True
        elif user_choice == 7:
            original_world, MAX_ROWS, MAX_COLUMNS = reader()
            correctValue = True
        else:
            print('Please re-enter selection')

    if turn == 0:
        print('Turn #', turn)

    # Call to the main functions that implement the game of life and death:
    afterBirth_world = only_birth(original_world, MAX_ROWS, MAX_COLUMNS)
    afterDeath_world = death_world(original_world, MAX_ROWS, MAX_COLUMNS)
    # Final world is acquired by merging after birth and death worlds:
    final_world = finalWorld(afterBirth_world, afterDeath_world)
    # Call to display functions:
    display(original_world, final_world, MAX_ROWS, MAX_COLUMNS)

    # while loop that runs until game has been quit:
    while not game_over:
        user_decision = input("Hit enter to continue ('q' to quit): ")

        # Keeps track of rounds:
        if user_decision == '':
            turn += 1

        # Done so that turn is not printed twice at the start:
        if turn > 0 and user_decision != 'q' and user_decision != 'Q':
            print('Turn #', turn)

        # When user chooses to advance to the next turn then the rules of birth and death are applied to the
        # new world we had attained in the previous round making it the starting/initial world/biosphere for our next
        # call to the functions:
        if user_decision == '':
            original_world = final_world
            afterBirth_world = only_birth(original_world, MAX_ROWS, MAX_COLUMNS)
            afterDeath_world = death_world(original_world, MAX_ROWS, MAX_COLUMNS)
            final_world = finalWorld(afterBirth_world, afterDeath_world)
            display(original_world, final_world, MAX_ROWS, MAX_COLUMNS)
        elif user_decision == 'd' or user_decision == 'D':
            print('<<< DEBUG messages ON! >>>')
            print('Information about original world: ')
            debugMode(original_world, MAX_ROWS, MAX_COLUMNS)
        elif user_decision == 'q' or user_decision == 'Q':
            game_over = True


# Call to the start() function:
start()
