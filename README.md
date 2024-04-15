# Project 1: Tic Tac Toe Game

## Description

The project is a multiplayer game of the famous Tic Tac Toe (played as human vs human) constituted of the following 11 functions and each one has a specific job to do:
    1- main(): As it’s called it’s the main function;
    2- intro(): This function introduces the rules of the game Tic Tac Toe;
    3- create_grid(): This function creates a blank 3x3 playboard;
    4- sym(): This function decides the players' symbols;
    5- startGaming(): This function starts the game;
    6- isFull(): This function check if the board is full;
    7- outOfBoard(): This function tells the players that their selection is out of range;
    8- printPretty(): This function prints the board nice;
    9- isWinner(): This function checks if anyone of the players is winning;
    10- illegal(): This function checks if the square picked has already been picked before;
    11- report(): This function gives the game summary;

When the program is executed, the players are introduced to the rules and after reading them they simply hit the “Enter” button in order to choose their symbols. After that, in order to select where each player wants to put his symbol, they have to choose a 1st number from 0 to 2 to select a column and the same thing is done for selecting their 2nd number so that the chosen symbol is placed and here comes the job of the functions mentioned previously. If any mistakes are made, then functions related to warn or inform the players about their mistakes will be executed.
