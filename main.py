from matrix import Matrix
from getData import import_data


def main():
    print("Dokładność do 5 liczby po przecinku.")
    matrix = Matrix(import_data())
    matrix.findInverseMatrix()
    matrix.printInverseMatrix()


if __name__ == "__main__":
    main()
