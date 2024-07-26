import os
from typing import LiteralString
from dotenv import load_dotenv
import pandas as pd
import json
import datetime
import logging
import requests
import os

load_dotenv()
API_KEY_RATES = os.getenv("API_KEY_RATES")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = - %(name)s - %(levelname)s - %(message)s",
    filename="../log/utils.txt",
    filemode="w",encoding="utf8")

greeting_logger = logging.getLogger("greeting")
info_cards_logger = logging.getLogger("get_card_number_mask")
top_transactions_logger = logging.getLogger("top_transactions")
cashback_logger = logging.getLogger("get_cashback")
expenses_logger = logging.getLogger("get_expenses_all_sum")
exchange_rates_logger = logging.getLogger("get_exchange_rates")


def greetings_user():
    time = datetime.datetime.now().hour
    greeting_logger.info("Фукнция запустилась")
    if time == range(0, 7):
        return "Доброй ночи"
    elif time == range(6, 13):
        return "Доброе утро"
    elif time == range(12, 20):
        return "Добрый день"
    else:
        return "Добрый вечер"


def get_card_number_mask(info_card: pd.DataFrame) -> list[dict]:
    '''Функция принимает DataFrame и маскирует карты.'''
    card = info_card.groupby("Номер карты", as_index=False).head(4)
    result = card.loc[:, ["Номер карты"]]
    info_cards_logger.info("Функция запустилась")
    return result.to_dict(orient="records")


def get_expenses_all_sum(info_expenses: pd.DataFrame) -> list:
    '''Функция принимает DataFrame и выводит общую сумму расходов.'''
    info = info_expenses.sort_values(by="Сумма платежа").head()
    amount = info.loc[:, ["Сумма платежа"]]
    expenses_logger.info("Функция запустилась")
    return amount.to_dict(orient="records")


def get_cashback(list_cashback: pd.DataFrame) -> list:
    """Функция принимает DataFrame и выводит Сумму платежа и Кэшбэк"""
    cashback = list_cashback.groupby("Кэшбэк", as_index=False)
    result = cashback.sum().loc[:, ["Сумма платежа", "Кэшбэк"]]
    cashback_logger.info("Функция запустилась")
    return result.to_dict(orient="records")


def top_transaction(transaction: pd.DataFrame) -> LiteralString | str:
    """Функция принимает DataFrame и выводит топ 5 транзакций"""
    top_5_operation = transaction.sort_values(by="Сумма платежа").head()
    information = top_5_operation.loc[:, ["Дата платежа", "Сумма платежа", "Категория", "Описание"]]
    top_transactions_logger.info("Функция запустилась")
    csv = information.to_dict(orient="records")
    return csv


def open_json():
    with open("../data/user_settings.json", encoding="utf-8") as f:
        load_json_info = json.load(f)


def get_exchange_rates(rates: list) -> list:
    pass


def share_price(price: dict) -> dict:
    pass


if __name__ == '__main__':
    exel_cashback = pd.read_excel("../data/operations.xlsx")
    exel_transaction = pd.read_excel("../data/operations.xlsx")
    exel_card = pd.read_excel("../data/operations.xlsx")
    exel_all_sum = pd.read_excel("../data/operations.xlsx")
    print(get_exchange_rates(load_j))
    print(greetings_user())
    print(top_transaction(exel_transaction))
    print(get_cashback(exel_cashback))
    print(get_card_number_mask(exel_card))
    print(get_expenses_all_sum(exel_all_sum))