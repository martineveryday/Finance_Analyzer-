class FinanceAnalyzer:
    @staticmethod
    def calculate_expenses(df, col):
        """Calculate total expenses from a DataFrame."""
        return df[col].sum()

    @staticmethod
    def split_into_categories(df,category,calc_col):
        """Split transactions into categories and return a dictionary of DataFrames."""
        per_category = df.groupby(category)[calc_col].sum().reset_index()
        per_category.rename(columns={calc_col: 'Amount Spent'}, inplace=True)

        return per_category


    @staticmethod
    def calculate_income(*args):
        """Calculate total income from multiple sources."""
        return sum(args)

    @staticmethod
    def calculate_diff(income, expenses):
        """Calculate the difference between income and expenses."""
        return float(income) - float(expenses)
