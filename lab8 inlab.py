import random
from breezypythongui import EasyFrame
class GuessingGame(EasyFrame):
 """Plays a guessing game with the user."""
 def __init__(self):
 """Sets up the window, widgets, and data."""
 EasyFrame.__init__(self, title = "Guessing Game")
 # Initialize the instance variables for the data
 self.myNumber = random.randint(1, 100)
 self.count = 0
 # Create and add widgets to the window
 greeting = "Guess a number between 1 and 100."
 self.hintLabel = self.addLabel(text = greeting,
 row = 0, column = 0,
 sticky = "NSEW",
 columnspan = 2)
 self.addLabel(text = "Your guess", row = 1, column = 0)
 self.guessField = self.addIntegerField(0, row = 1, column = 1)
 # Buttons have no command attributes yet
 self.nextButton = self.addButton(text = "Next", row = 2,
 column = 0)
 self.newButton = self.addButton(text = "New game",
 row = 2, column = 1)
def main():
 """Instantiate and pop up the window."""
 GuessingGame().mainloop()
 if __name__ == "__main__":
  main()