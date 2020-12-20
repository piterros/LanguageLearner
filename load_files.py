import csv
import glob
from settings import CSV_FILES
from collections import defaultdict

class LoadFiles:

    def load_csv_files(self):
        files = glob.glob(CSV_FILES + '/*.csv')
        words_dict = defaultdict(dict)
        for file_name in files:
            csv_data = csv.reader(open(file_name), delimiter=';')
            for words in csv_data:
                title = file_name.strip('.csv').split('/')[-1]
                words_dict[title].update({words[0]: words[1]})
        return words_dict
                # print(words)
            # print(list(csv_data))
            # print(file.strip('.csv').split('/')[-1])


            # words[file.strip('.csv').split('/')[-1]].update({data[0]: data[1]})
            # for data in csv_data:
            #     print(data[0])
                # for title in titles:
                #     words[title].update({data[0]: data[1]})

        # print(words_dict)

class GetTitle:
    pass
#     def get_title(self):
#         files = glob.glob(CSV_FILES + '/*.csv')
#
#         return titles