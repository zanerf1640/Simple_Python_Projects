"""
This is a simple fractal tree generator using Python's turtle graphics module.
It creates a visual representation of a fractal tree by recursively drawing branches.
This script is to reinforce understanding of recursion and graphical programming.

Author: Zane Francis
"""
import turtle
import random

def draw_branch(t, branch_length, angle, depth):
    if depth == 0 or branch_length < 5:
        return
    
    # Draw the main branch
    t.forward(branch_length)

    # randomize the angle and length
    angle_variation = random.uniform(-15, 15)
    length_variation = random.uniform(0.7, 0.9)
    new_length = branch_length * length_variation
    new_angle = angle + angle_variation

    # Draw the right branch
    t.right(new_angle)
    draw_branch(t, new_length, new_angle, depth - 1)
    t.left(new_angle)

    # Draw the left branch
    t.left(new_angle)
    draw_branch(t, branch_length, new_angle, depth - 1)
    t.right(new_angle)

    # Go back to the previous position
    t.backward(branch_length)

def main():
    # Set up the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.left(90)  # Point the turtle upwards
    t.up()
    t.backward(100)  # Move the turtle to the starting position
    t.down()
    t.color("green")
    t.pensize(2)
    # Draw the fractal tree
    draw_branch(t, branch_length=100, angle=30, depth=5)
    # Finish up
    turtle.done()

if __name__ == "__main__":
    main()