from matrix import Matrix
def main():
    testMatrix = [[-1,2,1],[2,-3,1],[-2,7,9]]
    matrix = Matrix(testMatrix)
    matrix.findInverseMatrix()
    matrix.printInverseMatrix()


if __name__ == "__main__":
    main()
