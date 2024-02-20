"""Taller evaluable"""

import glob
import re

import pandas as pd
from pandas import DataFrame


def load_input(input_directory: str) -> DataFrame:
    filenames = glob.glob(input_directory + '/*.*')
    dataframes = [
        pd.read_csv(filename, sep='§', index_col=None, names=['text'])
        for
        filename in filenames
    ]
    dataframe = pd.concat(dataframes).reset_index(drop=True)
    return dataframe


def clean_text(dataframe: DataFrame):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #

    dataframe = dataframe.copy()
    dataframe = dataframe['text'].replace(r'[\.,\/#!$%\^&\*;:{}=\-_`~()\['
                                          r'\]]', '',
                                          regex=True).apply(str.lower).apply(
        str.strip)
    return dataframe


def count_words(dataframe: DataFrame) -> DataFrame:
    pass


def save_output(dataframe: DataFrame, output_filename: str) -> None:
    pass
    """Save output to a file."""


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    dataframe = load_input(input_directory)
    dataframe = clean_text(dataframe)
    print(dataframe)
    dataframe = count_words(dataframe)
    save_output(dataframe, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
