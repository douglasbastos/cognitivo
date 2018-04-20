import csv
from datetime import datetime

from cognitivo.config import PROJECT_ROOT, DBSession
from cognitivo.models import PriceQuote


def run():
    with open(f'{PROJECT_ROOT}/files/price_quote.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        session = DBSession()

        for row in reader:
            print(f"Insering row {row['tube_assembly_id']}")
            row['bracket_pricing'] = True if row['bracket_pricing'] == 'Yes' else False
            row['quote_date'] = datetime.strptime(row['quote_date'], '%Y-%m-%d')
            session.add(PriceQuote(**row))
            session.commit()

        session.close()


if __name__ == '__main__':
    run()
