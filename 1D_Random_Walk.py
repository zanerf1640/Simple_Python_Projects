"""
This is a simple project reflecting the 1D Random walk concept.
The random walk can be best explained as a number of steps taken in random directions. Each step is of equal length, 
and the direction of each step is determined randomly.
In this implementation of a 1D random walk, we will simulate a walker starting at position 0 and taking a series of steps 
either to the left (-1) or to the right (+1) based on random choice. 
We will be using a coin flip mechanism to decide the direction of each step.

Author: Zane Francis
"""

import random
import matplotlib.pyplot as plt

def random_walk_1d(steps):
    # Starting position
    position = 0 
    # List to store the position at each step
    walk =[position]

    for _ in range(steps):
        # Move right
        step = 1 
        # Coin flip to decide direction
        if random.randint(0,1) == 0: 
            # Move left
            step = -1
        # Update position
        position += step 
        # Record the new position
        walk.append(position)
    return walk

# Function to plot the random walk
def plot_walk(walk):
    plt.figure(figsize=(10, 6))
    plt.plot(walk)
    plt.title("1D Random Walk")
    plt.xlabel("Number of Steps")
    plt.ylabel("Position")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Number of steps for the random walk
    num_steps = 10000
    walk = random_walk_1d(num_steps)
    plot_walk(walk)
    print(f"Final position after {num_steps} steps: {walk[-1]}")
