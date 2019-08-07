#include "Problem15.hpp"


long Problem15() {
    int size = 20;
    vector<vector<long> > recVector(size+1, vector<long>(size+1,0));
    long solution_reciprocal = reciprocalArray(size, size, recVector);
    cout << "Reciprocal approach: " << solution_reciprocal << endl;
    
    long solution_bottomUp = bottomUp(size, size);
    cout << "Bottom up approach: " << solution_bottomUp << endl;
    
    long solution_factorial = binomial(size);
    
    return solution_reciprocal;
}

long reciprocalArray (int i, int j, vector<vector<long> > &array) {
    if (i==0 || j==0){return 1;}
    if (array[i][j] != 0) {return array[i][j];}
    array[i][j] = reciprocalArray(i-1,j,array) + reciprocalArray(i,j-1,array);
    return array[i][j];
}

long bottomUp (int i, int j) {
    vector<vector<long>> paths(i+1,vector<long>(j+1,0));
    for (int k=0; k<=i; k++) {
        for (int l=0; l<=j; l++) {
            if (k==0 || l==0) {paths[k][l] = 1; continue;}
            paths[k][l] = paths[k-1][l] + paths[k][l-1];
        }
    }
    return paths[i][j];
}

long binomial(int size) {
    return factorial(2*size, size) / factorial(size);
}

// NOTE: Here, even long long is overfloating.
// One has to use an iterative technique so that multiplication can be done step by step.
// I did not implement this here, but it can be done easily.
long long factorial(int size, int cutOff){
    long long product = 1;
    for (int i=size; i>cutOff; i--) {
        product *= i;
    }
    return product;
}
