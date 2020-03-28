import numpy as np


class Sudoku:
    def __init__(self,s):
        self.mtxStack = [np.zeros((9,9), dtype=np.int8)]
        for i in range(9):
            for j in range(9):
                pos = 9*i+j
                if s[pos] != 0:
                    self.mtxStack[-1][i][j] = s[pos]
        print(self.mtxStack[-1])

    def getNumbers(self,row,col):
        numbers = set([0])
        numbers = numbers.union(self.mtxStack[-1][row])
        numbers = numbers.union(self.mtxStack[-1][:, col])
        f = lambda x: x//3 * 3
        box = self.mtxStack[-1][f(row):f(row)+3, f(col):f(col)+3]
        numbers = numbers.union(box.flatten())
        numbers.discard(0)
        return numbers
        
    def getNewNumber(self,row,col):
        numbers = self.getNumbers(row,col)
        if len(numbers)==8:
            s = set(range(1,10))
            target = s.difference(numbers)
            self.mtxStack[-1][row][col] = list(target)[0]
            return True
        return False

    def guessNewNumber(self):
        for row in range(9):
            for col in range(9):
                if self.mtxStack[-1][row][col] == 0:
                    numbers = self.getNumbers(row,col)
                    if len(numbers) == 7:
                        s = set(range(1,10))
                        target = s.difference(numbers)
                        prevMtx, self.mtxStack = self.mtxStack[-1], self.mtxStack[:-1]
                        for i in range(2):
                            newMtx = prevMtx.copy()
                            newMtx[row][col] = list(target)[i]
                            self.mtxStack.append(newMtx)
                        return True
        return False

    def correctSolution(self):
        for row in range(9):
            numbers = set(self.mtxStack[-1][row])
            if len(numbers) != 9:
                return False
        for col in range(9):
            numbers = set(self.mtxStack[-1][:,col])
            if len(numbers) != 9:
                return False
        for boxRow in range(0,3,6):
            for boxCol in range(0,3,6):
                numbers = set(self.mtxStack[-1][boxRow:boxRow+3, boxCol:boxCol+3].flatten())
                if len(numbers) != 9:
                    return False
        return True
            
    def findSolution(self):
        while self.mtxStack[-1].sum()<405:
            numberDeduced = False
            numberGuessed = False
            for i in range(9):
                for j in range(9):
                    if self.mtxStack[-1][i][j] == 0:
                        if self.getNewNumber(i,j):
                            numberDeduced = True

            if not numberDeduced:
                numberGuessed = self.guessNewNumber()

            if not numberDeduced and not numberGuessed:
                self.mtxStack = self.mtxStack[:-1]

        if self.correctSolution():
            print(self.mtxStack[-1])
            return self.mtxStack[-1][0,0]*100+self.mtxStack[-1][0,1]*10+self.mtxStack[-1][0,2]


def readFile():
    with open('p096_sudoku.txt','r') as f:
        file = f.read().splitlines()
        for i in file:
            if len(i) == 9:
                sudokustring += i
            else:
                sudokustring = ''
            if len(sudokustring) == 81:
                yield sudokustring


def main():
    sol = 0
    for sudokustring in readFile():
        SudokuInstance = Sudoku(sudokustring)
        sol+=SudokuInstance.findSolution()
    print(sol)

if __name__ == '__main__':
    main()