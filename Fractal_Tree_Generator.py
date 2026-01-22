"""
This is a simple fractal tree generator using Python's turtle graphics module.
It creates a visual representation of a fractal tree by recursively drawing branches.
This script is to reinforce understanding of recursion and graphical programming.

Author: Zane Francis
"""
import turtle
import random
import math
import sys

def draw_branch(t, branch_length, angle, depth):
    if depth == 0 or branch_length < 5:
        return
    
    # Draw the main branch
    t.forward(branch_length)

    # randomize the angle and length
    angle_variation = random.uniform(-15, 15)
    length_variation = random.uniform(0.7, 0.9)
    new_length = branch_length * length_variation
    