from file_handler import FileLoader
from data_manipulation import FinanceAnalyzer

def main():
    files = FileLoader('bank1.csv')
    dfs = files.read_csv_files()

    bank = dfs['bank1']

    bank_expenses = FinanceAnalyzer.calculate_expenses(bank, 'Withdrawals')
    bank_categories = FinanceAnalyzer.split_into_categories(bank,'Category', 'Withdrawals')

    return bank_expenses, bank_categories



if __name__ == "__main__":
    expenses, categories = main()
    print(f"Expenses Total: {expenses:.2f}")
    print(f"{categories}")


