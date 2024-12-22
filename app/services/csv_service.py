import csv
import itertools

def read_data_from_csv(path: str, batch_size: int = 250):
    with open(path, 'r', encoding='iso-8859-1') as file:
        csv_reader = csv.DictReader(file)
        batch = iter(csv_reader)
        while True:
            batch_data = list(itertools.islice(batch, batch_size))
            if not batch_data:
                break
            yield batch_data