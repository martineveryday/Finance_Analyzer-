import pandas as pd

class FileLoader:

    def __init__(self, *args):
        self.files = list(args)

    def read_csv_files(self):

        dfs = {f.replace(".csv", ""): pd.read_csv(f) for f in self.files if f.endswith(".csv")}

        return dfs
    