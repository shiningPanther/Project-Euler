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




/*
 Thoughts for solving the problem:
 1. As a test of prinicple, we first solve the problem without any further rules, where the result should be 2.5% on each square. This should give us an intuition after how many turns we reach this distribution
 2. This problem could be solved quite easily if we were not to consider any history of the previous moves. Then one only has to add up the possiblitites after each move. However, there are two rules that require the recording of the history of previous moves:
   i) The go to jail after throwing three consecutive pairs
   ii) The taking of any card a putting it back at the bottom of the pile, i.e. the order of the CH and CC piles.
  i) has a great influence on the possibility distribution: For six-sided dice it adds (1/6)^3 = 0.5%, for four-sided dice (1/4)^3 = 1.6% possibility to and the term on the jail file. ii) should not influence the outcome very much. We will therefore include i) and neglect ii) and see how close we get to the values given for 6-sided dice.
 */

#include "Problem84.h"
#include <iostream>
using namespace std;


int Problem84() {
    
    // NoFurtherRules(); // Conclusion from this function: After 100 turns the possibilities do not vary significantly anymore - 100 turns run in 6 ms.
    CompleteRules();
    return 101524;
}




/*
 In order to change between the six-sided dice and four-sided dice just comment and uncomment the respective probabilities of the dice throws.
 
 After 200 turns, the probability values for the largest fields are: 10 - 6.22%, 24 - 3.18%, 0 - 3.09% and therefore very close (identical except for a slight difference of field 10) to the given values.
 The time to evaluate the 200 turns including printing the probabilities after each turn is 35 ms on my computer.
 */

void CompleteRules() {
    // We divide the probability distributions as follows: If no pairs have been thrown in a row, the labels are marked from 0 to 39, if one pair has been thrown they are marked from 40 to 70 and if two pairs have been thrown in a row, they are marked from 80 to 119
    double probDistBeforeTurn[120] = {1}; // The probability distributions for each square
    double probDistAfterTurn[120] = {0};
    
    // These are the dice probabilities for six-sided dice
    //double diceWithoutDoubles[11] = {0, 2./36, 2./36, 4./36, 4./36, 6./36, 4./36, 4./36, 2./36, 2./36, 0}; // Probability distributions of the two six-sided dices exlcuding the same number on each dice
    //double diceOnlyDoubles[11] = {1./36, 0, 1./36, 0, 1./36, 0, 1./36, 0, 1./36, 0, 1./36}; // Probabitlity distribution of the two six-sided dices including only the double values
    // These are the dice probabilities for four-sided dice
    double diceWithoutDoubles[7] = {0, 2./16, 2./16, 4./16, 2./16, 2./16, 0};
    double diceOnlyDoubles[7] = {1./16, 0, 1./16, 0, 1./16, 0, 1./16};
    
    // Change this number as well when changing between six- and four-sided dice
    //int sidesOfDice = 6;
    int sidesOfDice = 4;
    
    int numberOfSquares = 119; // We have 119 effective squares, including the counting of thrown pairs in a row
    int jailSquare = 10;
    int cc1 = 2; int cc2 = 17; int cc3 = 33; // The community chest squares
    int ch1 = 7; int ch2 = 22; int ch3 = 36; // The chance squares
    
    int turns = 200; // Number of turns to be simulated
    double probSum = 0; // This is a number to check if the probablities add up to 1 after each turn
    
    // In each turn check where a player could possibly be before the turn. If a player can be on a particular field simulate each move he can make from this field with the according possiblity
    for (int turn = 1; turn <= turns; turn++) {
        // Now go through all the squares a player can be on
        for (int square = 0; square <= numberOfSquares; square++) {
            if (probDistBeforeTurn[square] != 0) {
                // Now go through all the possible dice combinations
                for (int number = 2; number <= 2*sidesOfDice; number++) {
                    int squareAdjusted; // squareAdjusted is just the same as square but it is adjusted to prevent accessing squares > 39
                    squareAdjusted = determineSquareNew(square, number);
                    int newSquare = (squareAdjusted + number) % 40; // The new square after a turn for non-doubles. Only squares from 0 to 39 are possible since any number larger than that would mean that there was at least one double in a row before.
                    int newSquareDouble = squareAdjusted + number + 40; // The new square after a turn for doubles
                    
                    // Go to jail because of three doubles in a row!!
                    if (newSquareDouble > 119) {newSquareDouble = jailSquare;}
                    
                    // Go to jail square
                    if (newSquare == 30) {newSquare = jailSquare;}
                    if (newSquareDouble == 70 || newSquareDouble == 110) {newSquareDouble = jailSquare;}
                    
                    // Chance
                    if (newSquare == ch1 || newSquare == ch2 || newSquare == ch3) {
                        // the squares after chance
                        int squareAfterCH[10] = {0};
                        // the probabilities to get on these squares, not yet including the dice probabilities
                        double probabilityAfterCH[10] = {0};
                        
                        // This is only done for newSquare, not for newSquareDouble --> The doubles get implemented manually later on
                        chance(newSquare, squareAfterCH, probabilityAfterCH);
                        
                        for (int i = 0; i < 10; i++) {
                            // First the probabilities without doubles
                            probDistAfterTurn[squareAfterCH[i]] += probabilityAfterCH[i] * probDistBeforeTurn[square] * diceWithoutDoubles[number - 2];
                            // Now probabilities with doubles - make sure that we go to jail if we had three doubles in a row...
                            if (newSquareDouble != jailSquare) {
                                // Use integer division to see how many times you have had a double already
                                if (newSquareDouble / 40 == 1) {
                                    probDistAfterTurn[squareAfterCH[i]+40] += probabilityAfterCH[i] * probDistBeforeTurn[square] * diceOnlyDoubles[number - 2];
                                }
                                if (newSquareDouble / 40 == 2) {
                                    probDistAfterTurn[squareAfterCH[i]+80] += probabilityAfterCH[i] * probDistBeforeTurn[square] * diceOnlyDoubles[number - 2];
                                }
                            }
                        }
                        // Let's go to jail if we had three doubles in a row...
                        if (newSquareDouble == jailSquare) {
                            probDistAfterTurn[newSquareDouble] += probDistBeforeTurn[square] * diceOnlyDoubles[number -2];
                        }
                        // This is number of the dice is done, we don't want to caculate the other probability distributions...
                        continue;
                    }
                    
                    // Community chest
                    if (newSquare % 40 == cc1 || newSquare % 40 == cc2 || newSquare % 40 == cc3) {
                        // the squares after community chess
                        int squareAfterCC[3] = {0};
                        // the probabilities to get on these squares, not yet including the dice probabilities
                        double probabilityAfterCC[3] = {0};
                        
                        communityChest(newSquare, squareAfterCC, probabilityAfterCC);
                        
                        for (int i = 0; i < 3; i++) {
                            // First the probabilities without doubles
                            probDistAfterTurn[squareAfterCC[i]] += probabilityAfterCC[i] * probDistBeforeTurn[square] * diceWithoutDoubles[number - 2];
                            // Now probabilities with doubles - make sure that we go to jail if we had three doubles in a row...
                            if (newSquareDouble != jailSquare) {
                                // Use integer division to see how many times we had a double already
                                if (newSquareDouble / 40 == 1) {
                                    probDistAfterTurn[squareAfterCC[i]+40] += probabilityAfterCC[i] * probDistBeforeTurn[square] * diceOnlyDoubles[number - 2];
                                }
                                if (newSquareDouble / 40 == 2) {
                                    probDistAfterTurn[squareAfterCC[i]+80] += probabilityAfterCC[i] * probDistBeforeTurn[square] * diceOnlyDoubles[number - 2];
                                }
                            }
                        }
                        // Let's go to jail if we had three doubles in a row...
                        if (newSquareDouble == jailSquare) {
                            probDistAfterTurn[newSquareDouble] += probDistBeforeTurn[square] * diceOnlyDoubles[number -2];
                        }
                        // This is number of the dice is done, we don't want to caculate the other probability distributions...
                        continue;
                    }
                    
                    // Now we calculate the possibility distributions for the case that we did not land on a cc or ch square
                    probDistAfterTurn[newSquare] += probDistBeforeTurn[square] * diceWithoutDoubles[number - 2];
                    probDistAfterTurn[newSquareDouble] += probDistBeforeTurn[square] * diceOnlyDoubles[number -2];
                    
                }
                probDistBeforeTurn[square] = 0; // Set this to 0 so that probabilities do not add up from the last turn
            }
        }
        
        // Just for printing the results (it cannot be done in the above loop since the calculations are not yet finished there)
        probSum = 0;
        cout << "After turn " << turn << ":\n";
        for (int square = 0; square <= 39; square++) {
            probSum += probDistAfterTurn[square] + probDistAfterTurn[square+40] + probDistAfterTurn[square+80];
            cout << probDistAfterTurn[square] + probDistAfterTurn[square+40] + probDistAfterTurn[square+80] << " ";
        }
        cout << "\nTotal probability: " << probSum << "\n";
        
        // Interchange the variables probDistBeforeTurn and probDistAfterTurn and set probDistAfterTurn to 0. This takes up unnecessary computation time and could be solved better - see example below in function NoFurtherRules. However, like this the readability is improved and computation times are still reasonable.
        for (int square = 0; square <= numberOfSquares; square++) {
            if (probDistAfterTurn[square] != 0) {
                probDistBeforeTurn[square] = probDistAfterTurn[square];
                probDistAfterTurn[square] = 0;
            }
        }
    }
    printResults(probDistBeforeTurn);
}

// If square + number <= 39 (or 79, or 119) then this function just returns square. If square + number > 39 (or 79 or 119), then this function returns square-40.
int determineSquareNew(int square, int number) {
    // This has to be adjusted
    if (square < 40 && square + number > 39) {return square - 40;}
    if (square < 80 && square + number > 79) {return square - 40;}
    if (square < 120 && square + number > 119) {return square - 40;}
    return square;
}

void communityChest(int square, int squareAfterCC[3], double probsAfterCC[3]) {
    // Advance to Go --> set square to 0, 40, 80
    squareAfterCC[0] = 0;
    probsAfterCC[0] = 1./16;
    
    // Go to Jail --> set square to 10, 50, 90
    squareAfterCC[1] = 10;
    probsAfterCC[1] = 1./16;
    
    // If nothing happens --> set square to original square
    squareAfterCC[2] = square;
    probsAfterCC[2] = 7./8;
}

void chance(int square, int squareAfterCH[10], double probsAfterCH[10]) {
    // Advance to Go --> set square to 0, 40, 80
    squareAfterCH[0] = 0;
    probsAfterCH[0] = 1./16;
    
    // Go to Jail --> set square to 10, 50, 90
    squareAfterCH[1] = 10;
    probsAfterCH[1] = 1./16;
    
    // Go to C1 --> set square to 11, 51, 91
    squareAfterCH[2] = 11;
    probsAfterCH[2] = 1./16;
    
    // Go to E3 --> set square to 24, 64, 104
    squareAfterCH[3] = 24;
    probsAfterCH[3] = 1./16;
    
    // Go to H2 --> set square to 39, 79, 119
    squareAfterCH[4] = 39;
    probsAfterCH[4] = 1./16;
    
    // Go to R1 --> set square to 5, 45, 85
    squareAfterCH[5] = 5;
    probsAfterCH[5] = 1./16;
    
    // Go to next R (5, 15, 25, 35) --> two cards, i.e. chance of 1/8
    if (square < 5) {squareAfterCH[6] = 5;}
    else if (square < 15) {squareAfterCH[6] = 15;}
    else if (square < 25) {squareAfterCH[6] = 25;}
    else if (square < 35) {squareAfterCH[6] = 35;}
    else if (square < 40) {squareAfterCH[6] = 5;}
    probsAfterCH[6] = 1./8;
    
    // Go to next U (12, 28)
    if (square < 12) {squareAfterCH[7] = 12;}
    else if (square < 28) {squareAfterCH[7] = 28;}
    else if (square < 40) {squareAfterCH[7] = 12;}
    probsAfterCH[7] = 1./16;
    
    // Go back 3 squares
    squareAfterCH[8] = square - 3;
    probsAfterCH[8] = 1./16;
    
    // If nothing happens --> set square to original square
    squareAfterCH[9] = square;
    probsAfterCH[9] = 3./8;
}

void printResults(double probDistribution[120]) {
    double probs[40];
    for (int i = 0; i < 40; i++) {
        *(probs +i) = *(probDistribution + i) + *(probDistribution + 40+i) + *(probDistribution + 80+i);
    }
    
    // Print largest values
    double largest1 = 0.;
    int pos1 = 0;
    for (int i = 0; i < 40; i++) {
        if (*(probs + i) > largest1) {
            largest1 = *(probs + i);
            pos1 = i;
        }
    }
    cout << pos1 << ": " << largest1*100 << "%\n";
    
    // Print 2nd largest position
    double largest2 = 0.;
    int pos2 = 0;
    for (int i = 0; i < 40; i++) {
        if (*(probs + i) > largest2) {
            if (i != pos1) {
                largest2 = *(probs + i);
                pos2 = i;
            }
        }
    }
    cout << pos2 << ": " << largest2*100 << "%\n";
    
    // Print 3rd largest position
    double largest3 = 0.;
    int pos3 = 0;
    for (int i = 0; i < 40; i++) {
        if (*(probs + i) > largest3) {
            if (i != pos1 && i != pos2) {
                largest3 = *(probs + i);
                pos3 = i;
            }
        }
    }
    cout << pos3 << ": " << largest3*100 << "%\n";
    
    // Print 4th largest position
    double largest4 = 0.;
    int pos4 = 0;
    for (int i = 0; i < 40; i++) {
        if (*(probs + i) > largest4) {
            if (i != pos1 && i != pos2 && i != pos3) {
                largest4 = *(probs + i);
                pos4 = i;
            }
        }
    }
    cout << pos4 << ": " << largest4*100 << "%\n";
    
    // Print 5th largest position
    double largest5 = 0.;
    int pos5 = 0;
    for (int i = 0; i < 40; i++) {
        if (*(probs + i) > largest5) {
            if (i != pos1 && i != pos2 && i != pos3 && i != pos4) {
                largest5 = *(probs + i);
                pos5 = i;
            }
        }
    }
    cout << pos5 << ": " << largest5*100 << "%\n";
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
