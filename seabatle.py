import random

# Set up the game area
game_area = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(' ')
    game_area.append(row)

# Define the ship lengths
ship_lengths = [1, 2, 3, 4]

# Generate three random ships
for i in range(3):
    # Choose a random length for the ship
    ship_length = random.choice(ship_lengths)

    # Choose a random starting position for the ship
    x = random.randint(0, 10 - ship_length)
    y = random.randint(0, 10 - ship_length)

    # Choose a random orientation for the ship (0 for horizontal, 1 for vertical)
    orientation = random.randint(0, 1)

    # Place the ship on the game area
    for j in range(ship_length):
        if orientation == 0:
            game_area[y][x + j] = 'S'
        else:
            game_area[y + j][x] = 'S'

# Play the game
num_guesses = 0
while True:
    # Print the game area
    print('  0123456789')
    for i in range(10):
        row_str = str(i) + ' '
        for j in range(10):
            row_str += game_area[i][j]
        print(row_str)

    # Get a guess from the user
    guess = input('Enter your guess (row, column): ')
    row = int(guess[0])
    col = int(guess[2])

    # Check if the guess hit a ship
    if game_area[row][col] == 'S':
        print('Hit!')
        game_area[row][col] = 'X'
    else:
        print('Miss!')
        game_area[row][col] = 'O'

    # Count the number of guesses
    num_guesses += 1

    # Check if all the ships have been sunk
    all_sunk = True
    for i in range(10):
        for j in range(10):
            if game_area[i][j] == 'S':
                all_sunk = False
    if all_sunk:
        print('You won in', num_guesses, 'guesses!')
        break