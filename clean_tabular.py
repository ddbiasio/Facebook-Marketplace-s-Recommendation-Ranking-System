import pandas as pd

class CleanTabular:

    def __init__(self, file_path: str, line_terminator: str = None):
        self.data_to_clean: pd.DataFrame = None
        pd.set_option('display.max_columns', None)
        if line_terminator:
            self.data_to_clean = pd.read_csv(file_path, lineterminator=line_terminator)
        else:
            self.data_to_clean = pd.read_csv(file_path)

    def clean_currency(self, curr_field: str):

        # Make the price convertible to float
        self.data_to_clean[curr_field] = self.data_to_clean[curr_field].str.strip("£")
        self.data_to_clean[curr_field] = self.data_to_clean[curr_field].str.replace(",","")
        try:
            # Convert to float
            self.data_to_clean[curr_field] = self.data_to_clean[curr_field].astype(float)
        except ValueError as ve:
            print(f"{self.data_to_clean[curr_field]} cannot be converted to float: {str(ve.args[0])}")

    def clean_emojis(self, text_field: str):

        # strip out non-ascii chars
        self.data_to_clean[text_field] = (
            self.data_to_clean[text_field].apply(
                lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x])))

    def make_lower_case(self, text_field: str):

        # make all text in specified field lower case
        self.data_to_clean[text_field] = self.data_to_clean[text_field].str.lower()

    def split_data(self, text_field: str, sep: str, index: int, new_column: str = None):

        
        # split the data using sep annd get data from index position
        if new_column:
            # create a new column if specified
            self.data_to_clean[new_column] = self.data_to_clean[text_field].str.split(sep).str[index]
        else:
            # otherwwise overwrite existing value
            self.data_to_clean[text_field] = self.data_to_clean[text_field].str.split(sep).str[index]
    
    def make_categorical(self, text_field: str, new_column: str = None):

        if new_column:
            # create a new column if specified
            self.data_to_clean[new_column] = (
                self.data_to_clean[text_field].astype('category').cat.codes.astype('int64'))
        else:
            # otherwwise overwrite existing value
            self.data_to_clean[text_field] = (
                self.data_to_clean[text_field].astype('category').cat.codes.astype('int64'))   

    def write_clean_file(self, file_name: str,  line_terminator: str = None):
        self.data_to_clean.to_csv(file_name, line_terminator = line_terminator)