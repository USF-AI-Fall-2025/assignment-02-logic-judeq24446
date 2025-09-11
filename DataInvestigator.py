import pandas as pd

class DataInvestigator:
    def __init__(self, df):
        self.df = df
        self.col_nums = {} # empty dictionary to hold column indexes
        key = 0
        # loop through the columns and set the index to the label
        for c in df.columns:
            self.col_nums[key] = c
            key += 1

    # helper function to set the column indexes to labels
    def get_col_label(self, col):
        col_label = self.col_nums[col]
        return col_label
    
    def baseline(self, col):
        try:
            col_label = self.get_col_label(col) # get the column label from the index
            col_values = self.df[col_label] # get the column values from the column label
            value_counts = {} # empty dictionary to hold the value counts from the column
            for v in col_values:
                # count the occurrences of each value in the column
                if v in value_counts:
                    value_counts[v] += 1
                else:
                    value_counts[v] = 1
            max_count = 0 
            max_value = 0 # variable to hold the value with the highest count
            for val, count in value_counts.items():
                # find the value with the highest count
                if count > max_count:
                    max_count = count
                    max_value = val
            return max_value
        except: # in case of an error, return None
            return None

    def corr(self, col1, col2):
        try:
            # get the column labels from the indexes
            col_label1 = self.get_col_label(col1)
            col_label2 = self.get_col_label(col2)
            return self.df[col_label1].corr(self.df[col_label2])
        except: # in case of an error, return None
            return None

    def zeroR(self, col):
        return self.baseline(col)

df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)
print(di.baseline(1))
print(di.corr(2, 3))
print(di.zeroR(1))