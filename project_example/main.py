"""
Главный модуль для анализа корпуса текстов Dante's Inferno.

Этот скрипт анализирует все текстовые файлы в папке corpus/
и создаёт отчёты с результатами анализа.
"""

import os
from text_utils import (
    count_words,
    count_unique_words,
    calculate_ttr,
    get_most_common_words,
    count_lines,
    average_word_length
)
from file_utils import (
    read_text_file,
    read_csv_file,
    write_csv_file,
    write_text_file,
    get_files_in_folder
)


def analyze_single_text(filepath, filename):
    pass


def analyze_corpus(corpus_folder):
    pass


def generate_report(results, metadata):
   pass


def main():
    pass

if __name__ == "__main__":
    main()
