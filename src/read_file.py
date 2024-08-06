import logging
from typing import Any

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/reports.txt",
    filemode="w",
)

read_excel_logger = logging.getLogger("read_excel_file")


def read_excel_file(filename: str) -> Any:
    """Считывает данные с EXCEL файла и переобразовыввает их в JSON-формат"""
    read_excel_logger.info("Начали считывание информации с EXCEL-файла")
    try:
        operations = pd.read_excel(filename)
        operations = operations.where(pd.notnull(operations), operations.fillna("Отсутствует"))
        file_dict = operations.to_dict(orient="records")
        read_excel_logger.info("Окончили считывание информации с EXCEL-файла")
        return file_dict
    except Exception as e:
        read_excel_logger.error(f"Произошла ошибка {e} при считывание информации с EXCEL-файла")
        return f"Ошибка {e}. повторите попытку"


def read_defolt_exel(filename: str) -> Any:
    """Считывает данные с EXCEL файла"""
    df = pd.read_excel("../data/operations.xlsx")
    return df
