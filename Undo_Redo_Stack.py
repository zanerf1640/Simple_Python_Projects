"""
This is a simple program that shows the behavior of the stack data structure with undo and redo functionality.
We will implement a basic text editor that allows users to type text, undo their last action, and redo an undone action.
The program uses two stacks to keep track of the actions for undo and redo operations.

Author: Zane Francis
"""

def undo_redo_stack():
    # Undo stack for storing previous states
    undo_stack = []
    # Redo stack for storing states that can be redone
    redo_stack = []
    # Current text in the editor
    current_text = ""

    print("---Simple Text Editor with Undo/Redo---")

    while True:
        print("\nCurrent Text:", current_text)
        print("Options:")
        print("1. Type Text")
        print("2. Undo")
        print("3. Redo")
        print("4. View Current Text Stack")
        print("5. View Undo Stack")
        print("6. View Redo Stack")
        print("7. Exit")

        # Get user choice
        choice = input("Choose an option (1-7): ")

        # Handles adding text to the editor
        if choice == '1':
            text_to_add = input("Enter text to add: ")
            undo_stack.append(current_text)
            current_text += text_to_add
            redo_stack.clear()
            print("Text added.")
        # Handles undo operation
        elif choice == '2':
            if undo_stack:
                redo_stack.append(current_text)
                current_text = undo_stack.pop()
                print("Undo performed.")
            else:
                print("Nothing to undo!")
        # Handles redo operation
        elif choice == '3':
            if redo_stack:
                undo_stack.append(current_text)
                current_text = redo_stack.pop()
                print("Redo performed.")
            else:
                print("Nothing to redo!")
        # Displays the current text
        elif choice == '4':
            print("\nCurrent Text:", current_text)
        # Displays the undo stack
        elif choice == '5':
            print("\nUndo Stack:", undo_stack)
        # Displays the redo stack
        elif choice == '6':
            print("\nRedo Stack:", redo_stack)
        # Handles exiting the program
        elif choice == '7':
            print("Exiting the text editor. Goodbye!")
            break
        # Handles invalid choices
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    undo_redo_stack()