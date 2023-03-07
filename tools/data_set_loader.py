import os

from data import DataSet


class DataSetLoader:

    @staticmethod
    def load_data_set(file_path: str,
                      ignore_bad_rows: bool = False, have_column_names: bool = False,
                      separator: str = ",", row_separator: str = "\n") -> DataSet:
        if not os.path.isfile(file_path):
            raise Exception("Can`t find file")

        data = []
        column_names = None
        if have_column_names:
            column_names = []
        columns_len = 0

        with open(file_path, 'r') as file:
            content = file.read()

            rows = content.split(row_separator)

            for index, row in enumerate(rows):
                columns = row.split(separator)

                if index == 0:                          # prepare
                    columns_len = len(columns)          # calculate columns count only on first row
                    if columns_len > 1:
                        for _ in range(columns_len):    # fill data empty columns lists
                            data.append([])

                    # if file have columns
                    if have_column_names:
                        column_names = columns
                        continue

                elif len(columns) != columns_len:
                    if ignore_bad_rows:
                        continue
                    else:
                        raise Exception("Receive invalid row. [{0}]".format(row))

                if columns_len == 1:
                    data.append(columns[0])
                    continue

                for c in range(columns_len):
                    data[c].append(columns[c])

        return DataSet(file_path, data, column_names)
