#include "Problem67.hpp"

int Problem67() {
    vector<vector<int> > numbers;
    ifstream myfile("/Users/peter/Documents/Coding/Project Euler/p067_triangle.txt");
    if (myfile.is_open())
    {
        string line;
        int rownumber = 0;
        while (getline(myfile,line))
        {
            int columnnumber = 0;
            istringstream iss(line);
            while(iss) {
                int number;
                iss >> number;
                if (rownumber >= columnnumber) {
                    if (columnnumber == 0) {
                        numbers.push_back(vector<int>(rownumber+1,number));
                    }
                    else {numbers[rownumber][columnnumber] = number;}
                }
                columnnumber++;
            }
            rownumber++;
        }
        myfile.close();
    }
    
    for (int i=int(numbers.size())-2; i>=0; i--) {
        for (int j=0; j<=i; j++) {
            numbers[i][j] = numbers[i][j] + max(numbers[i+1][j], numbers[i+1][j+1]);
        }
    }
    return numbers[0][0];
}
