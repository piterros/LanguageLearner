# from create_dicts import CreateDict
from load_files import LoadFiles

load_files = LoadFiles()

load_files.get_title()
# load_files.load_csv_files()
# for x in load_files.get_title():
#     print(x)
for x in load_files.load_csv_files():
    print(x)

# create_dict = CreateDict()
#
# create_dict.create_dict()