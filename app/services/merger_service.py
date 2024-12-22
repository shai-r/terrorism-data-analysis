import pandas as pd
import os
import itertools
from typing import List

current_directory = os.getcwd()

sources_directory = os.path.join(current_directory,  'sources')
file_1 = os.path.join(sources_directory, 'RAND_Database_of_Worldwide_Terrorism_Incidents.csv')
file_2 = os.path.join(sources_directory, 'globalterrorismdb_0718dist.csv')


def clean_data(df):
    df = df.where(pd.notnull(df), "")
    if 'eventid' in df.columns:
        df['eventid'] = df['eventid'].apply(lambda x: str(x) if x is not None else None)
    return df


def merger(file1: str, file2: str) -> List[dict]:
    df1 = pd.read_csv(file1, encoding='iso-8859-1')
    df2 = pd.read_csv(file2, encoding='iso-8859-1')
    df1['year'] = df1['Date'].str[-4:].astype(float, errors='ignore')
    df1['month'] = pd.to_numeric(df1['Date'].str[3:6].map({"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
                                                            "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                                                            "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}), errors='coerce')
    df1['day'] = pd.to_numeric(df1['Date'].str[:2], errors='coerce')

    df1['year'] = pd.to_numeric(df1['year'], errors='coerce', downcast='integer')
    df1['month'] = pd.to_numeric(df1['month'], errors='coerce', downcast='integer')
    df1['day'] = pd.to_numeric(df1['day'], errors='coerce', downcast='integer')

    df2['iyear'] = pd.to_numeric(df2['iyear'], errors='coerce', downcast='integer')
    df2['imonth'] = pd.to_numeric(df2['imonth'], errors='coerce', downcast='integer')
    df2['iday'] = pd.to_numeric(df2['iday'], errors='coerce', downcast='integer')
    merged_df = pd.merge(
        df2,
        df1,
        how="left",
        left_on=["city", "country_txt", "iyear", "imonth", "iday"],
        right_on=["City", "Country", "year", "month", "day"]
    )

    merged_df['Weapon'] = merged_df['Weapon'].combine_first(merged_df['weaptype1_txt'])
    merged_df['Description'] = merged_df['Description'].combine_first(merged_df['summary'])

    merged_df = clean_data(merged_df)

    return list(merged_df.to_dict(orient='records'))


def send_data_in_batches(batch_size: int = 200):
    batch = iter(merger(file_1, file_2))
    while True:
        batch_data = list(itertools.islice(batch, batch_size))
        if not batch_data:
            break
        yield batch_data
