class Matrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.inverse = [[0 for x in range(len(matrix[0]))]for x in range(len(matrix))]
        for x in range(len(self.inverse)):
            for y in range(len(self.inverse[x])):
                if x != y:
                    self.inverse[x][y]=0
                else:
                    self.inverse[x][y]=1
        pass

    def findInverseMatrix(self):
        self.checkSwaps()
        for x in range(len(self.matrix)):
            self.divideRow(x,1/self.matrix[x][x])
            for y in range(len(self.matrix)):
                if y != x:
                    self.substractRow(y,x,self.matrix[y][x]/self.matrix[x][x])

    def checkSwaps(self):
        for x in range(len(self.matrix)):
            if self.matrix[x][x]==0:
                for y in range(len(self.matrix)):
                    if self.matrix[y][x]!=0 and self.matrix[x][y] != 0:
                        self.swapRows(x,y)
                        break
                    elif y==len(self.matrix)-1:
                        print("Dla podanej macierzy nie da się ustalić macierzy odwrotnej.")
                        exit()

    def swapRows(self,swap1,swap2):
        for x in range(len(self.matrix[swap1])):
            tmp = self.matrix[swap1][x]
            self.matrix[swap1][x]=self.matrix[swap2][x]
            self.matrix[swap2][x] = tmp

    def printInverseMatrix(self):
        for x in range(len(self.inverse)):
            for y in range(len(self.inverse[x])):
                print(self.inverse[x][y],end=" ")
            print("")

    def substractRow(self,subFrom,tosub,howManyTimes):
        for x in range(len(self.matrix[subFrom])):
            self.matrix[subFrom][x]-=self.matrix[tosub][x]*howManyTimes
            self.inverse[subFrom][x] -= self.inverse[tosub][x]*howManyTimes

    def divideRow(self,divideFrom,divider):
        for x in range(len(self.matrix[divideFrom])):
            self.matrix[divideFrom][x]*=divider
            self.inverse[divideFrom][x]*=divider