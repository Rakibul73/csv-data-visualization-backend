import pandas as pd
from app import db, Data, app

def clean_data(df):
    for column in ['open', 'high', 'low', 'close']:
        df[column] = df[column].str.replace(',', '').astype(float)
    df['volume'] = df['volume'].str.replace(',', '').astype(int)
    return df

with app.app_context():
    # Create the tables
    db.create_all()
    
    # Read and clean the CSV data
    df = pd.read_csv('stock_market_data.csv')
    df = clean_data(df)

    # Insert the data into the database
    for index, row in df.iterrows():
        db.session.add(Data(
            trade_code=row['trade_code'],
            date=row['date'],
            open=row['open'],
            high=row['high'],
            low=row['low'],
            close=row['close'],
            volume=row['volume']
        ))
    db.session.commit()
    print("Database populated successfully.")
