import matplotlib.pyplot as plt
import numpy as np

# Creating an empty board with default dimensions 5x5
m, n = 5, 5
board_array = np.zeros((m, n))

# Plotting the empty board
fig, ax = plt.subplots()
cax = ax.matshow(board_array, cmap='coolwarm')

# Adding grid lines to distinguish fields
for (i, j), val in np.ndenumerate(board_array):
    ax.text(j, i, f'{val}', ha='center', va='center', color='black')

# Setting tick labels
ax.set_xticklabels([''] + list(range(n)))
ax.set_yticklabels([''] + list(range(m)))

plt.title('Empty Board Visualization')
plt.show()

