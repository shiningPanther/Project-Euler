//
//  Project Euler - Problem 54
//
//  POKER HANDS

#include "Problem54.hpp"

int Problem54() {
    ifstream myfile("/Users/peter/Documents/Coding/Project Euler/problem54_poker");
    int winsPlayer1 = 0;
    if (myfile.is_open())
    {
        string line;
        while (getline(myfile,line))
        {
            //cout << line << '\n';
            if (player1Won(line)) {
                winsPlayer1++;
            }
        }
        myfile.close();
    }
    
    return winsPlayer1;
}

bool player1Won(string cards) {
    
    map<char, int> player1_cards = createMap(cards, 0);
    map<char, int> player1_suit = createMap(cards, 1);
    map<char, int> player2_cards = createMap(cards, 15);
    map<char, int> player2_suit = createMap(cards, 16);
    
    // Rank corresponds to the goodness of the cards: 0 --> high card, 9 --> straight flush
    int player1Rank = determineRank(player1_cards, player1_suit);
    int player2Rank = determineRank(player2_cards, player2_suit);
    if (player1Rank > player2Rank) {return true;}
    
    if (player1Rank == player2Rank) {
        if (player1Rank == 0) {
            int player1HighCard = getHighCard(player1_cards);
            int player2HighCard = getHighCard(player2_cards);
            if (player1HighCard > player2HighCard) {return true;}
            else if (player1HighCard == player2HighCard) {cout << " No winner could be found" << endl;}}
        if (player1Rank == 1) {
            int player1Pair = getPairRank(player1_cards);
            int player2Pair = getPairRank(player2_cards);
            if (player1Pair > player2Pair) {return true;}
            if (player1Pair == player2Pair) {
                int player1HighCard = getHighCard(player1_cards);
                int player2HighCard = getHighCard(player2_cards);
                if (player1HighCard > player2HighCard) {return true;}
                else if (player1HighCard == player2HighCard) {cout << "No winner could be found" << endl;}}}
        if (player1Rank > 1) {cout << "No winner could be found" << endl;}
    }
    
    return false;
}

map<char, int> createMap(string cards, int startValue) {
    map<char, int> map;
    int i = startValue;
    while (i<=startValue+12) {
        char key = cards[i];
        if (map.count(key)) { map[key]++; }
        else { map[key] = 1; }
        i+=3;
    }
    return map;
}

int determineRank(map<char,int> cards, map<char,int> suit) {
    int rank = 0;
    if (isAtLeastPair(cards)) {
        rank = 1;
        if (isAtLeastTwoPairs(cards)) {
            rank = 2;
            if (isFullHouse(cards)) {
                rank = 6;
            }
        }
        else if (isAtLeastThreeOfAKind(cards)) {
            rank = 3;
            if (isFourOfAKind(cards)) {
                rank = 7;
            }
        }
    }
    else if (isFlush(suit)) {
        rank = 5;
    }
    else if (isStraight(cards)) {
        rank = 4;
    }
    return rank;
}

bool isAtLeastPair(map<char,int> cards) {
    for (auto iter : cards) {
        if (iter.second >= 2) {return true;}
    }
    return false;
}

bool isAtLeastTwoPairs(map<char,int> cards) {
    bool pair1 = false;
    bool pair2 = false;
    for (auto iter : cards) {
        if (iter.second >= 2) {
            if (pair1 == true) {pair2 = true;}
            else {pair1 = true;}
        }
    }
    if (pair1 == true && pair2 == true) {return true;}
    return false;
}

bool isFullHouse(map<char,int> cards) {
    bool triple = false;
    bool pair = false;
    for (auto iter : cards) {
        if (iter.second == 2) {pair = true;}
        if (iter.second == 3) {triple = true;}
    }
    if (pair == true && triple == true) {return true;}
    return false;
}

bool isAtLeastThreeOfAKind(map<char,int> cards) {
    for (auto iter : cards) {
        if (iter.second >= 3) {return true;}
    }
    return false;
}

bool isFourOfAKind(map<char,int> cards) {
    for (auto iter : cards) {
        if (iter.second == 4) {return true;}
    }
    return false;
}
             
 bool isFlush(map<char,int> suit) {
     if (suit.begin()->second == 5) {return true;}
     return false;
 }

bool isStraight(map<char,int> cards) {
    if (cards.count('2') && cards.count('3') && cards.count('4') && cards.count('5') && cards.count('6')) {return true;}
    if (cards.count('7') && cards.count('3') && cards.count('4') && cards.count('5') && cards.count('6')) {return true;}
    if (cards.count('7') && cards.count('8') && cards.count('4') && cards.count('5') && cards.count('6')) {return true;}
    if (cards.count('7') && cards.count('8') && cards.count('9') && cards.count('5') && cards.count('6')) {return true;}
    if (cards.count('7') && cards.count('8') && cards.count('9') && cards.count('T') && cards.count('6')) {return true;}
    if (cards.count('7') && cards.count('8') && cards.count('9') && cards.count('T') && cards.count('J')) {return true;}
    if (cards.count('Q') && cards.count('8') && cards.count('9') && cards.count('T') && cards.count('J')) {return true;}
    if (cards.count('Q') && cards.count('K') && cards.count('9') && cards.count('T') && cards.count('J')) {return true;}
    if (cards.count('Q') && cards.count('K') && cards.count('A') && cards.count('T') && cards.count('J')) {return true;}
    return false;
}

int getPairRank(map<char,int> cards) {
    for (auto iter : cards) {
        if (iter.second == 2) {
            if (iter.first == '3') {return 3;}
            else if (iter.first == '4') {return 4;}
            else if (iter.first == '5') {return 5;}
            else if (iter.first == '6') {return 6;}
            else if (iter.first == '7') {return 7;}
            else if (iter.first == '8') {return 8;}
            else if (iter.first == '9') {return 9;}
            else if (iter.first == 'T') {return 10;}
            else if (iter.first == 'J') {return 11;}
            else if (iter.first == 'Q') {return 12;}
            else if (iter.first == 'K') {return 13;}
            else if (iter.first == 'A') {return 14;}
        }
    }
    return 2;
}

int getHighCard(map<char,int> cards) {
    int highCard = 2;
    for (auto iter : cards) {
        if (iter.second == 1) {
            if (iter.first == '3') {if (3>highCard) {highCard = 3;}}
            if (iter.first == '4') {if (4>highCard) {highCard = 4;}}
            if (iter.first == '5') {if (5>highCard) {highCard = 5;}}
            if (iter.first == '6') {if (6>highCard) {highCard = 6;}}
            if (iter.first == '7') {if (7>highCard) {highCard = 7;}}
            if (iter.first == '8') {if (8>highCard) {highCard = 8;}}
            if (iter.first == '9') {if (9>highCard) {highCard = 9;}}
            if (iter.first == 'T') {if (10>highCard) {highCard = 10;}}
            if (iter.first == 'J') {if (11>highCard) {highCard = 11;}}
            if (iter.first == 'Q') {if (12>highCard) {highCard = 12;}}
            if (iter.first == 'K') {if (13>highCard) {highCard = 13;}}
            if (iter.first == 'A') {if (14>highCard) {highCard = 14;}}
        }
    }
    return highCard;
}
