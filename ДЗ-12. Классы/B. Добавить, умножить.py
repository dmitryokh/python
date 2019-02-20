import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


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

    def __add__(self, other):
        rez = []
        if Matrix.size(self) != Matrix.size(other):
            error = MatrixError(self, other)
            raise error
        for i in range(len(self.matrix)):
            rez.append([])
            for j in range(len(self.matrix[i])):
                rez[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(rez)

    def __mul__(self, n):
        rez = []
        for i in range(len(self.matrix)):
            rez.append([])
            for j in range(len(self.matrix[i])):
                rez[i].append(n * self.matrix[i][j])
        return(Matrix(rez))

    __rmul__ = __mul__

    def transpose(self):
        t_matrix = list(zip(*self.matrix))
        self.matrix = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        t_matrix = list(zip(*self.matrix))
        return Matrix(t_matrix)

exec(stdin.read())
