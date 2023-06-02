from matrix import Matrix
from getData import import_data


def main():
    matrix = Matrix(import_data())
    matrix.findInverseMatrix()
    print("Dokładność do 7 liczby po przecinku.\nMacierz odwrotna:")
    matrix.printInverseMatrix()


if __name__ == "__main__":
    main()
