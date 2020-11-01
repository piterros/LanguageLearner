import csv
import glob
from settings import CSV_FILES

class LoadFiles:

    def load_csv_files(self):
        file_list = glob.glob(CSV_FILES + '/*.csv')
        for file in file_list:
            csv_data = csv.reader(open(file), delimiter=';')
            for data in csv_data:
                yield data

    def get_title(self):
        for title in self.load_csv_files():
            print('title', title)
            dict_title = next(title)
            yield dict_title

    def get_words(self):
        for word in self.load_csv_files():
            print(word)
