# Cellular-Automata
Implement Conway's Game of Life
This code is implementing the Game of Life, a cellular automaton invented by John Horton Conway in 1970. It is a zero-player game, meaning that once it is set up, it runs on its own according to a set of rules.

The Game of Life is played on a grid of cells, where each cell can be in one of two states: "on" or "off". The game follows a set of rules to determine the next state of each cell, based on the current state of the cell and the states of its eight neighbors (the cells that are horizontally, vertically, or diagonally adjacent to it).

The rules for the Game of Life are:

Any live cell with fewer than two live neighbors dies, as if by underpopulation.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
