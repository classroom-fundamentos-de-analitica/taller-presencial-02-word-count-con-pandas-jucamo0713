"""Taller evaluable"""

import glob

import pandas as pd
from pandas import DataFrame


def load_input(input_directory: str) -> DataFrame:
    filenames = glob.glob(input_directory + '/*.*')
    dataframes = [
        pd.read_csv(filename, sep=';', index_col=None, names=['text'])
        for
        filename in filenames
    ]
    dataframe = pd.concat(dataframes).reset_index(drop=True)
    return dataframe


def clean_text(dataframe: DataFrame):
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe['text'].replace(
        r'[\.,\/#!$%\^&\*;:{}=\_`~(#)\[\]]',
        '',
        regex=True).apply(str.lower).apply(str.strip)
    return dataframe


def count_words(dataframe: DataFrame) -> DataFrame:
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.split(' ')
    dataframe = dataframe.explode('text').reset_index(drop=True)
    dataframe = dataframe.rename(columns={'text': 'word'})
    dataframe['count'] = 1
    dataframe = dataframe.groupby(['word']).agg(
        {
            'count': 'sum'
        }
    )
    return dataframe


def save_output(dataframe: DataFrame, output_filename: str) -> None:
    dataframe.to_csv(output_filename, sep='\t')


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    dataframe = load_input(input_directory)
    dataframe = clean_text(dataframe)
    dataframe = count_words(dataframe)
    save_output(dataframe, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
