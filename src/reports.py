import datetime
import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/reports.txt",
    filemode="w",
)

decorator_logger = logging.getLogger("spending_result")
spending_by_category_logger = logging.getLogger("spending_by_category")


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
    sort_transaction = transactions.sort_values(by="Дата платежа", ascending=False)

    if date is None:
        date = datetime.datetime.now().strftime("%d.%m.%Y")

    date_split = date.split(".")
    three_months_ago = int(date_split[1]) - 4

    date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
    date_three_month_ago = date_obj.replace(month=three_months_ago)

    slice_ = date_three_month_ago.strftime("%d.%m.%Y")

    file_to_data = sort_transaction[
        (sort_transaction["Дата платежа"] >= slice_) & (sort_transaction["Дата платежа"] <= date)
        ]

    sort_by_category = file_to_data[(file_to_data["Категория"] == category)]

    spending_by_category_logger.info("Функция запустилась")
    return pd.DataFrame(sort_by_category)