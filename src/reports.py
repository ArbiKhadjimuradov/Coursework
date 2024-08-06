import datetime
import datetime as dt
import logging
from pathlib import Path

import pandas as pd
from src.read_file import read_excel_file, read_defolt_exel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/reports.txt",
    filemode="w",
)

decorator_logger = logging.getLogger("spending_result")
spending_by_category_logger = logging.getLogger("spending_by_category")

ROOT_PATH = Path(__file__).resolve().parent.parent


def spending_result(path_file: str = "../data/test_to_operation.xlsx"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result.to_csv(path_file)

            decorator_logger.info("декоратор отработал, записал результат функции в файл")

            return result

        return wrapper

    return decorator


@spending_result()
def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца."""
    if date is None:
        fin_data = dt.datetime.now()
    else:
        fin_data = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    start_data = fin_data.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=91)
    transactions_by_category = transactions.loc[
        (pd.to_datetime(transactions["Дата операции"], dayfirst=True) <= fin_data)
        & (pd.to_datetime(transactions["Дата операции"], dayfirst=True) >= start_data)
        & (transactions["Категория"] == category)
        ]
    return transactions_by_category


operation = read_excel_file("../data/operations.xlsx")
if __name__ == "__main__":
    result = spending_by_category(read_defolt_exel(str(ROOT_PATH) + "../data/operations.xlsx"), "Аптеки",
                                  "26.07.2019 20:58:55")
    print(result)
