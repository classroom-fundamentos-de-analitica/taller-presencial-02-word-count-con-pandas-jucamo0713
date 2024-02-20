"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    pass
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #


def clean_text(dataframe):
    pass
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #


def count_words(dataframe):
    pass
    """Word count"""


def save_output(dataframe, output_filename):
    pass
    """Save output to a file."""


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
