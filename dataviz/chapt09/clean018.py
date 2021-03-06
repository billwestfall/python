import pandas as pd
import numpy as np
from pymongo import MongoClient

df = pd.read_json(open("data/nobel_winners_dirty.json"))

def clean_data(df):
    bi_col = df['born_in']
    print("Describe born in column")
    print(df.born_in.describe())
    print("Setting born in to unicode")
    set(df.born_in.apply(type))
    print(set(df.born_in.apply(type)))
    bi_col.replace('', np.nan, inplace=True)
    print("Replace missing values with NaN")
    print(bi_col)
    print(bi_col.count())
    print("Replace names with asterisk with emptry string")
    df.name = df.name.str.replace('*', '')
    df.name = df.name.str.strip()
    print(df.name)
    print("verify no asterisks")
    print(df[df.name.str.contains('\*')])

    print("find number of null entries")
    df = df[df.born_in.isnull()]
    print(df.count())
    dupes_by_name = df[df.duplicated('name')]
    print("find duplicate name entries")
    print(dupes_by_name.count())

    all_dupes = df[df.duplicated('name') | df.duplicated('name', keep='last')]
    print("all duplicate entries sorted by name")
    print(all_dupes.sort_values('name') [['name', 'country', 'year']])

    print("count before dropping duplicates")
    print(df.count())
    df = df.reindex(np.random.permutation(df.index))
    df = df.drop_duplicates(['name', 'year'])
    df = df.sort_index()
    print("count after dropping dupes")
    print(df.count())

    print("show the remaining duplicate entries")
    valid_dupes = df[df.duplicated('name') | df.duplicated('name', keep='last')].sort_values(by='name')[['name', 'country', 'year', 'category']]
    print(valid_dupes)

    print("correct category field")
    df.ix[df.name == 'Alexis Carrel', 'category'] = 'Physiology or Medicine'
    print(df.count())

    print("entries with missing gender")
    miss_gend = df[df.gender.isnull()]['name']
    print(miss_gend)

    print("add missing gender and remove institutions")
    df.ix[df.name == 'Ragnar Granit', 'gender'] = 'male'
    df = df[df.gender.notnull()]
    print(df.count())

    print("unified date format")
    print(pd.to_datetime(df.date_of_birth, errors='raise'))

    print("catch date of death exceptions")

    for i,row in df.iterrows():
        try:
            pd.to_datetime(row.date_of_death, errors='raise')
        except:
            print('%s(%s, %d)'%(row.date_of_death.ljust(30), row['name'], i))

    print("set no death date to NaN")
    df.date_of_death = pd.to_datetime(df.date_of_death, errors='coerce')
    df.date_of_birth = pd.to_datetime(df.date_of_birth)

    df['award_age'] = df.year - pd.DatetimeIndex(df.date_of_birth).year

    print(df.sort_values('award_age').iloc[:10] [['name', 'award_age', 'category', 'year']])


def get_mongo_database(db_name, host='localhost', port='27017'):
    conn = MongoClient(host, port)
    return conn[db_name]

def dataframe_to_mongo(df, db_name, collection, host='localhost', port='27017'):
    db = get_mongo_database(db_name, host, port)

    records = df.to_dict('records')
    db[collection].insert(records)

df_clean, df_born_in = clean_data(df)

dataframe_to_mongo(df_clean, 'nobel_prize', 'winners')
dataframe_to_mongo(df_born_in, 'nobel_prize', 'winners_born_in')
