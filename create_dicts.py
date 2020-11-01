from load_files import LoadFiles
from collections import defaultdict

class CreateDict:

    def __init__(self):
        self.load_files = LoadFiles()

    def create_dict(self):
        dict_titles = {}
        for line in self.load_files.get_title():
            dict_titles[''.join(next(line))] = {}
        # print(dict_titles)
        return dict_titles

    # def add_data_to_dict(self):
    #     word_dict = defaultdict(set)
    #     for dictio in self.create_dict():
    #         word_dict[dictio].add()