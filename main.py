from matrix import Matrix
from getData import import_data


def main():
    matrix = Matrix(import_data())
    matrix.findInverseMatrix()
    matrix.printInverseMatrix()


if __name__ == "__main__":
    main()
