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
                        row.append(int(values[x]))
                    except ValueError:
                        print("Błąd: nie można przekonwertować wartości na liczby całkowite!")
                        exit()
                data.append(row)
    except FileNotFoundError:
        print("Błąd: plik nie istnieje!")
        exit()
    return data