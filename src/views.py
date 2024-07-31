import datetime
import json
import logging

import pandas as pd

from src.utils import get_card_number_mask, get_exchange_rates, greetings_user, share_price, top_transaction

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/views.txt",
    filemode="w",
)

opening_logger = logging.getLogger("opening_file")
views_logger = logging.getLogger("views")


def open_file(path_file: str) -> pd.DataFrame:
    """Функция читает файл формата xlsx и возвращает DataFrame"""
    operations_xlsx = pd.read_excel(path_file)

    opening_logger.info("Функция отработала")

    return operations_xlsx


def views(data: str) -> str:
    """Функция принимает дату и возвращает информацию за месяц."""
    info_file = open_file("../data/operations.xlsx")
    sort_file = info_file.sort_values(by="Дата платежа", ascending=True)

    views_logger.info("открытие файла успешно, open_file отработал")

    date_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
    new_date_obj = date_obj.replace(day=1)

    time_last = date_obj.strftime("%d.%m.%Y")
    time_first = new_date_obj.strftime("%d.%m.%Y")

    sort_by_data = sort_file[(sort_file["Дата платежа"] >= time_first) & (sort_file["Дата платежа"] <= time_last)]

    views_logger.info("Сортировка платежа по дате")

    with open("../user_settings.json", encoding="utf-8") as f:
        load_json = json.load(f)

    views_logger.info("Открылся файл")

    information = dict()

    information["greeting"] = greetings_user()
    views_logger.info("greeting_user запустился")

    information["cards"] = get_card_number_mask(sort_by_data)
    views_logger.info("get_card_number_mask запустился")

    information["top_transactions"] = top_transaction(sort_by_data)
    views_logger.info("top_transaction запустился")

    information["currency_rates"] = get_exchange_rates(load_json["user_currencies"])
    views_logger.info("get_exchange_rates запустился")

    information["stock_prices"] = share_price(load_json["user_stocks"])
    views_logger.info("share_price запустился")

    return json.dumps(information, ensure_ascii=False, indent=3)


if __name__ == "__main__":
    print(views("20.10.2022"))
