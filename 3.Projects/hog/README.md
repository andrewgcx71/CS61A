![](https://media.giphy.com/media/AhS5br4fmV322i0DvA/giphy.gif)


Introduction
-----

This project involves developing a simulator and multiple strategies for the dice game Hog.

Rules
-----

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes. However, a player who rolls too many dice risks:

**Pig Out.** If any of the dice outcomes is a 1, the current player's score for the turn is 1.
In a normal game of Hog, those are all the rules. To spice up the game, we'll include some special rules:

**Free Bacon.** A player who chooses to roll zero dice scores points equal to one more than the absolute alternating difference of the digits of the opponent's score cubed.

**Feral Hogs.** If the number of dice you roll is exactly 2 away (absolute difference) from the number of points you scored on the previous turn, you get 3 extra points for the turn. Treat the turn before the first turn as scoring 0 points. Do not take into account any previous feral hog bonuses or swine swap (next rule) when calculating the number of points scored the previous turn.

**Swine Swap.** Define the excitement of the game to be three to the power of the sum of the players' scores. After points for the turn are added to the current player's score, if the excitement's first digit and last digit are the same, the scores should be swapped.

File
------

Files in the project:

- **hog.py:** A starter implementation of Hog
- **dice.py:** Functions for rolling dice
- **hog_gui.py:** A graphical user interface for Hog
- **ucb.py:** Utility functions for CS 61A
- **gui_files:** A directory of various things used by the web gui

Graphical User Interface
--------

To run the GUI from your terminal:

**python3 hog_gui.py**


Class Project Site
---

[here](https://inst.eecs.berkeley.edu/~cs61a/fa20/proj/hog/)
