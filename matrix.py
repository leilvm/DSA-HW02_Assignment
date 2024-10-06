# File: /dsa/sparse_matrix/code/src/sparse_matrix.py
class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        elif numRows and numCols:
            self.numRows = numRows
            self.numCols = numCols
            self.matrix = {}

    def load_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
        
        try:
            self.numRows = int(lines[0].split('=')[1])
            self.numCols = int(lines[1].split('=')[1])
            self.matrix = {}

            for line in lines[2:]:
                row, col, value = map(int, line.strip().strip('()').split(','))
                self.set_element(row, col, value)
        except Exception as e:
            raise ValueError("Input file has wrong format") from e

    def get_element(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)

    def set_element(self, currRow, currCol, value):
        if value != 0:
            self.matrix[(currRow, currCol)] = value
        elif (currRow, currCol) in self.matrix:
            del self.matrix[(currRow, currCol)]

    def add(self, otherMatrix):
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)

        for key in set(self.matrix.keys()).union(otherMatrix.matrix.keys()):
            row, col = key
            value = self.get_element(row, col) + otherMatrix.get_element(row, col)
            result.set_element(row, col, value)

        return result

    def subtract(self, otherMatrix):
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)

        for key in set(self.matrix.keys()).union(otherMatrix.matrix.keys()):
            row, col = key
            value = self.get_element(row, col) - otherMatrix.get_element(row, col)
            result.set_element(row, col, value)

        return result

    def multiply(self, otherMatrix):
        if self.numCols != otherMatrix.numRows:
            raise ValueError("Number of columns of first matrix must be equal to number of rows of second matrix")

        result = SparseMatrix(numRows=self.numRows, numCols=otherMatrix.numCols)

        for i in range(self.numRows):
            for j in range(otherMatrix.numCols):
                value = sum(self.get_element(i, k) * otherMatrix.get_element(k, j) for k in range(self.numCols))
                result.set_element(i, j, value)

        return result
