from asyncore import write
import random
from util.StochasticMatrix import StochasticMatrix
from util.file import writeNewLine

class Groups(StochasticMatrix):

    # default constructor
    def __init__(self, n):
        self.group = []
        for x in range(0, n):
            # Adds the amount of warrios per group
            groupName = 'Group ' + str(x + 1)
            self.group.append({'name': groupName, 'n': 50, 'index': x})
        super().__init__(n)

    def selectGroup(self):
        selectedGroup = random.randrange(0, len(self.group))
        return selectedGroup

    def selectGroupToAtack(self, indexAtacker):
        selectedGroup = random.uniform(0, 1)
        min = 0
        max = self.matrix[indexAtacker][0]
        defendersIndex = None
        for i, group in enumerate(self.matrix[indexAtacker]):
            if(selectedGroup > min and selectedGroup < max):
                defendersIndex = i
                return defendersIndex
            min = max
            max = max + self.matrix[indexAtacker][i+1]

    def groupRandomAtack(self):
        # Selects the index of the groups that will atack and defend respectively
        atackerIndex = self.selectGroup()
        defenderIndex = self.selectGroupToAtack(atackerIndex)
        atackerStr = 'Atacker: ' + self.group[atackerIndex]['name']
        defenderStr = 'Defender: ' + self.group[defenderIndex]['name']
        print(atackerStr)
        print(defenderStr)
        writeNewLine(atackerStr)
        writeNewLine(defenderStr)
        # Reduce the amount of troops to decrease in the defenders group
        self.group[defenderIndex]['n'] = max(
            self.group[defenderIndex]['n'] - self.group[atackerIndex]['n'], 0)

        # Removes the stochastic matrix index
        if(self.group[defenderIndex]['n'] <= 0):
            self.group.pop(defenderIndex)
            self.removeRowColumn(defenderIndex)
            # Updates the index reference in all the groups
            for i in range(0, len(self.group)):
                self.group[i]['index'] = i
            # Updates the values of the stochastic matrix
            self.populateMatrix()
