import csv
# import pandas as pd

with open('./sample/spanish/preterito_imperfecto_charakterytyczne_slowka.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=';')
    csv_title = next(csv_data)

    print('title', csv_title)
    for x in csv_data:
        print(x)