from .raw_reader import Raw_Reader

class Reader_Proxy:
    def __init__(self):
        pass

    def get_reader(read_file: str):
        return Raw_Reader(read_file)