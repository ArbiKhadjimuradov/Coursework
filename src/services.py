import logging
import re

from src.read_file import read_excel_file

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="log/services.txt",
    filemode="w",
    encoding="utf-8"
)

filter_by_number = logging.getLogger("filtering_by_search")

operation = read_excel_file("../data/operations.xlsx")


def filter_numbers(transaction: list) -> list:
    """Функция фильтрует список по номеру телефона в описании"""
    filter_by_number.info("Начали сортировку по номерам телефона")
    new_list_filter = []
    for i in transaction:
        if "Описание" in i and re.findall(
                r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", i["Описание"], flags=re.IGNORECASE
        ):
            new_list_filter.append(i)
    filter_by_number.info("Окончили сортировку по номерам телефона")
    return new_list_filter


if __name__ == "__main__":
    print(filter_numbers(operation))
