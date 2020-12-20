from load_files import LoadFiles
import random

class Quiz:

    def quiz(self, language='es'):
        load_files = LoadFiles()
        load_files.load_csv_files()
        for key, value in load_files.load_csv_files().items():
            if language == 'pl':
                yield key, random.sample(list(value.values()), 3)
            else:
                yield key, random.sample(list(value.keys()), 3)

