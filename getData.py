import math

def import_data():
    data = []
    try:
        with open("./data.txt") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                values = line.split()
                row = []
                for x in range(len(values)):
                    try:
                        if abs(float(values[x])) > math.pow(10, 20):
                            print(f"Liczba musi byc > {math.pow(10, 20)}. Błąd przy odczytie liczby {values[x]}")
                            exit()
                        row.append(float(values[x]))
                    except ValueError:
                        print(f"Błąd: nie można przekonwertować wartości {values[x]} na liczbę!")
                        exit()
                data.append(row)
    except FileNotFoundError:
        print("Błąd: plik nie istnieje!")
        exit()
    rows_count = len(data)
    for row in data:
        if len(row) != rows_count:
            print(f"Macierz nie jest kwadratowa. Liczba wierszy {rows_count}, liczba kolumn {len(row)}.")
            exit()

    return data