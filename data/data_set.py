
class DataSet:

    def __init__(self, real_file: str,  data: list, column_names: list = None):
        self.data = data
        self.real_file = real_file
        self.column_names = column_names
