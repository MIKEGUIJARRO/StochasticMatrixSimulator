import numpy as np
import random


class StochasticMatrix:

    # default constructor
    def __init__(self, n):
        self.n = n
        self.matrix = np.zeros((n, n))
        self.populateMatrix()

    def populateMatrix(self):
        # This method populates the matrix
        # following the principle of an stochastic matrix
        for i in range(0, len(self.matrix)):
            probabilityLeft = 100
            if(len(self.matrix) == 1):
                return
            for j in range(0, len(self.matrix[i])):
                if (i == j):
                    self.matrix[i][j] = 0
                    continue
                if (j == len(self.matrix[i]) - 1):
                    self.matrix[i][j] = round(probabilityLeft / 100, 2)
                    continue
                if(len(self.matrix) == 2 and i == len(self.matrix) - 1 and j == 0):
                    self.matrix[i][j] = 1
                    continue
                # Generates a random value %
                randValue = random.randrange(0, probabilityLeft)
                probabilityLeft = probabilityLeft - randValue
                self.matrix[i][j] = round(randValue / 100, 2)

    def removeRowColumn(self, index):
        # Removes column
        self.matrix = np.delete(self.matrix, index, axis=1)
        # Removes row
        self.matrix = np.delete(self.matrix, index, axis=0)

    def printMatrix(self):
        print(self.matrix)

    def isScalar(self):
        #Checks if the matrix is 1 x 1
        if(len(self.matrix) == 1): 
            return True
        else:
            return False