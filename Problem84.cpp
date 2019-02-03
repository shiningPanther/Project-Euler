/*
In the game, Monopoly, the standard board is set up in the following way:

GO    A1    CC1    A2    T1    R1    B1    CH1    B2    B3    JAIL
H2                                                            C1
T2                                                            U1
H1                                                            C2
CH3                                                           C3
R4                                                            R2
G3                                                            D1
CC3                                                           CC2
G2                                                            D2
G1                                                            D3
G2J    F3    U2    F2    F1    R3    E3    E2    CH2    E1    FP
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
 
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
 
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
 
 */

#include "Problem84.h"
#include <iostream>
using namespace std;




// Thoughts for solving the problem:
// 1. As a test of prinicple, we first solve the problem without any further rules, where the result should be 2.5% on each square. This should give us an intuition after how many turns we reach this distribution
// 2. This problem could be solved quite easily if we were not to consider any history of the previous moves. Then one only has to add up the possiblitites after each move. However, there are two rules that require the recording of the history of previous moves:
//   i) The go to jail after throwing three consecutive pairs
//   ii) The taking of any card a putting it back at the bottom of the pile, i.e. the order of the CH and CC piles.
//  i) has a great influence on the possibility distribution: For six-sided dice it adds (1/6)^3 = 0.5%, for four-sided dice (1/4)^3 = 1.6% possibility to and the term on the jail file. ii) should not influence the outcome very much. We will therefore include i) and neglect ii) and see how close we get to the values given for 6-sided dice.


int Problem84() {
    
    NoFurtherRules(); // Conclusion from this function: After 100 turns the possibilities do not vary significantly anymore - 100 turns run in 6 ms.
    CompleteRules();
    return 10;
}



void CompleteRules() {
    // We divide the probability distributions as follows: If no pairs have been thrown in a row, the labels are marked from 0 to 39, if one pair has been thrown they are marked from 40 to 70 and if two pairs have been thrown in a row, they are marked from 80 to 119
    double probDistBeforeTurn[120] = {1}; // The probability distributions for each square
    double sixSideDice[11] = {1./36., 2./36, 3./36, 4./36, 5./36, 6./36, 5./36, 4./36, 3./36, 2./36, 1./36};
    int sidesOfDice = 6;
    int numberOfSquares = 119; // We have 119 effective squares, including the counting of thrown pairs in a row
    
    int turns = 2; // Number of turns to be simulated - Note: turns = 1 corresponds to 2 moves by the player, turns = 2 to 4 moves, etc...
    double probSum = 0; // This is a number to check if the probablities add up to 1 after each turn
    
    // In each turn check where a player could possibly be and if a player can be on a particular field simulate each move he can make from this field with the according possiblity
    for (int turn = 1; turn <= turns; turn++) {
        double probDistAfterTurn[120];
        // Now go through all the squares a player can be on
        for (int square = 0; square <= numberOfSquares; square++) {
            if (probDistBeforeTurn[square] != 0) {
                // Now go through all the possible dice combinations
                for (int number = 2; number <= 2*sidesOfDice; number++) {
                    int squareNew; // squareNew is just the same as square but it is adjusted to prevent accessing squares > 39
                    squareNew = determineSquareNew(square, number);
                    probDistAfterTurn[squareNew+number] += probDistBeforeTurn[square] * sixSideDice[number - 2];
                }
                probDistBeforeTurn[square] = 0; // Set this to 0 so that probabilities do not add up from the last turn
            }
        }
        
        // Just for printing the results (it cannot be done in the above loop since the calculations are not yet finished there)
        probSum = 0;
        cout << "After turn " << turn << ":\n";
        for (int square = 0; square <= 39; square++) {
            probSum += probDistAfterTurn[square];
            cout << probDistAfterTurn[square] << " ";
        }
        cout << "\nTotal probability: " << probSum << "\n";
        
        // Interchange the variables probDistBeforeTurn and probDistAfterTurn and set probDistAfterTurn to 0. This takes up unnecessary computation time and could be solved better - see example below in function NoFurtherRules. However, like this the readability is improved...
        for (int square = 0; square <= numberOfSquares; square++) {
            if (probDistAfterTurn[square] != 0) {
                probDistBeforeTurn[square] = probDistAfterTurn[square];
                probDistAfterTurn[square] = 0;
            }
        }
        
        
    }
}

// If square + number <= 39 (or 79, or 119) then this function just returns square. If square + number > 39 (or 79 or 119), then this function returns square-40.
int determineSquareNew(int square, int number) {
    // This has to be adjusted
    if (square + number > 39) {squareNew = square - 40;} // This if clause prevents accessing squares >39
    else {squareNew = square;}
}


void NoFurtherRules() {
    double probDist1[40] = {1}; // The probability distributions for each square
    double probDist2[40]; // We need two to distinguish between before a move and after a move
    double sixSideDice[11] = {1./36., 2./36, 3./36, 4./36, 5./36, 6./36, 5./36, 4./36, 3./36, 2./36, 1./36};
    
    int turns = 50; // Number of turns to be simulated - Note: turns = 1 corresponds to 2 moves by the player, turns = 2 to 4 moves, etc...
    double probSum = 0; // This is a number to check if the probablities add up to 1 after each turn
    
    // In each turn check where a player could possibly be and if a player can be on a particular field simulate each move he can make from this field with the according possiblity
    for (int turn = 1; turn <= turns; turn++) {
        // Now go through all the squares a player can be on
        for (int square = 0; square <= 39; square++) {
            if (probDist1[square] != 0) {
                // Now go through all the possible dice combinations
                for (int number = 2; number <= 12; number++) {
                    int squareNew;
                    if (square + number > 39) {squareNew = square - 40;} // This if clause prevents accessing squares >39
                    else {squareNew = square;}
                    probDist2[squareNew+number] += probDist1[square] * sixSideDice[number - 2];
                }
                probDist1[square] = 0; // Set this to 0 so that probabilities do not add up from the last turn
            }
        }
        
        // Just for printing the results (it cannot be done in the above loop since the calculations are not yet finished there)
        probSum = 0;
        cout << "After turn " << 2*turn - 1 << ":\n";
            for (int square = 0; square <= 39; square++) {
                probSum += probDist2[square];
                cout << probDist2[square] << " ";
            }
        cout << "\nTotal probability: " << probSum << "\n";
        
        for (int square = 0; square <= 39; square++) {
            if (probDist2[square] != 0) {
                // Now go through all the possible dice combinations
                for (int number = 2; number <= 12; number++) {
                    int squareNew;
                    if (square + number > 39) {squareNew = square - 40;} // This if clause prevents accessing squares >39
                    else {squareNew = square;}
                    probDist1[squareNew+number] += probDist2[square] * sixSideDice[number - 2];
                }
                probDist2[square] = 0; // Set this to 0 so that probabilities do not add up from the last turn
            }
        }
    }
}
