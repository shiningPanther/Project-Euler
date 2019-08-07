#include <iostream>
#include <string>
#include <fstream>
#include <map>
using namespace std;

int Problem54();
bool player1Won(string);
map<char, int> createMap(string, int);
int determineRank(map<char,int>, map<char,int>);
bool isFlush(map<char,int>);
bool isFourOfAKind(map<char,int>);
bool isFullHouse(map<char,int>);
bool isAtLeastThreeOfAKind(map<char,int>);
bool isAtLeastPair(map<char,int>);
bool isAtLeastTwoPairs(map<char,int>);
bool isStraight(map<char,int>);
int getPairRank(map<char,int>);
int getHighCard(map<char,int>);
