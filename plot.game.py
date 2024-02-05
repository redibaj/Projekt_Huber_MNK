import matplotlib.pyplot as plt
import numpy as np

# Initialize an empty board with dimensions 5x5
board_size = 5
board_array = np.zeros((board_size, board_size))

# Simulate a sequence of moves for two players
# Player 1 is represented by 1, and Player 2 is represented by 2
# We'll simulate a few moves manually for illustration
moves = [
    (1, 1, 1),  # Player 1 moves at (1,1)
    (2, 2, 2),  # Player 2 moves at (2,2)
    (3, 3, 1),  # Player 1 moves at (3,3)
    (1, 2, 2),  # Player 2 moves at (1,2)
    (2, 1, 1),  # Player 1 moves at (2,1)
]

# Apply the moves to the board
for x, y, player in moves:
    # Adjusting for 0-based indexing and flipping the y-coordinate to match the array orientation
    board_array[5-y, x-1] = player

# Plotting the board after the simulated moves
fig, ax = plt.subplots()
cax = ax.matshow(board_array, cmap='coolwarm')

# Adding grid lines to distinguish cells, and labels to show player positions
for (i, j), val in np.ndenumerate(board_array):
    ax.text(j, i, f'{val}', ha='center', va='center', color='black' if val > 0 else 'grey')

# Adjust grid appearance
ax.set_xticks(np.arange(-.5, 5, 1), minor=True)
ax.set_yticks(np.arange(-.5, 5, 1), minor=True)
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.title('Simulated Game State Visualization')
plt.show()
