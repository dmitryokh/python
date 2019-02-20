import copy
from sys import stdin


class Matrix:
    def __init__(self, dlist):
        self.matrix = copy.deepcopy(dlist)

    def __str__(self):
        strng = ""
        for i in range(len(self.matrix) - 1):
            for j in range(len(self.matrix[i]) - 1):
                strng += str(self.matrix[i][j]) + "\t"
            strng += str(self.matrix[i][-1]) + "\n"
        for j in range(len(self.matrix[0]) - 1):
            strng += str(self.matrix[-1][j]) + "\t"
        strng += str(self.matrix[-1][-1])
        return(strng)

    def size(self):
        return(len(self.matrix), len(self.matrix[0]))

exec(stdin.read())
