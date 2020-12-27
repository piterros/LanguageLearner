import csv
import glob
from settings import CSV_FILES
from collections import defaultdict

class LoadFiles:
    """
    Loading files with questions and answers.
    """

    def load_csv_files(self) -> dict:
        """
        Loading CSV files with questions and answers.
        :returns:
            Dictionary with category of question as key and questions and answers as value.
        """
        files = glob.glob(CSV_FILES + '/*.csv')
        words_dict = defaultdict(dict)
        for file_name in files:
            csv_data = csv.reader(open(file_name), delimiter=';')
            for words in csv_data:
                title = file_name.strip('.csv').split('/')[-1]
                words_dict[title].update({words[0]: words[1]})
        return words_dict