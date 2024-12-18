from time import sleep

from app.services.csv_service import read_data_from_csv

import os

from app.services.save_sql_producer_service import save_in_sql_producer

current_directory = os.getcwd()

target_directory = os.path.join(current_directory, 'sources', 'globalterrorismdb_0718dist-1000 rows.csv')

print(os.path.abspath(target_directory))


if __name__ == '__main__':
    for a in read_data_from_csv(target_directory):
        save_in_sql_producer(a, "raw-data")