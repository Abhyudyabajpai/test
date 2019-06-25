from csv import reader
with open("read_csv.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
        