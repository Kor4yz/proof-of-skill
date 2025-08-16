import pandas as pd

def load(path='../data/transactions_sample.csv'):
    return pd.read_csv(path, parse_dates=['order_date'])

if __name__ == '__main__':
    df = load()
    print(df.head())
