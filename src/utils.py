import logging
import datetime
import json
import os
from typing import LiteralString

import freecurrencyapi
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY_RATES = os.getenv("API_KEY_RATES")
API_KEY_RA = os.getenv("API_KEY_CURRENCY")


greeting_logger = logging.getLogger("greeting")
info_cards_logger = logging.getLogger("get_card_number_mask")
top_transactions_logger = logging.getLogger("top_transactions")
cashback_logger = logging.getLogger("get_cashback")
expenses_logger = logging.getLogger("get_expenses_all_sum")
exchange_rates_logger = logging.getLogger("get_exchange_rates")
share_price_logger = logging.getLogger("share_price")


with open('../data/user_settings.json') as f:
    load_json = json.load(f)


def greetings_user():
    time = datetime.datetime.now().hour
    greeting_logger.info("Фукнция запустилась")
    if 0 <= time <= 7:
        return "Доброй ночи"
    elif 6 <= time <= 13:
        return "Доброе утро"
    elif 12 <= time <= 18:
        return "Добрый день"
    else:
        return "Добрый вечер"


def get_card_number_mask(info_card: pd.DataFrame) -> list[dict]:
    """Функция принимает DataFrame и маскирует карты."""
    card = info_card.groupby("Номер карты", as_index=False).head(1)
    result = card.loc[:, ["Номер карты", "Сумма платежа", "Кэшбэк"]]
    info_cards_logger.info("Функция запустилась")
    return result.to_dict(orient="records")


def top_transaction(transaction: pd.DataFrame) -> LiteralString | str:
    """Функция принимает DataFrame и выводит топ 5 транзакций"""
    top_5_operation = transaction.sort_values(by="Сумма платежа")
    information = top_5_operation.loc[:, ["Дата платежа", "Сумма платежа", "Категория", "Описание"]].head()
    top_transactions_logger.info("Функция запустилась")
    csv = information.to_dict(orient="records")
    return csv


def get_exchange_rates(rates_list: list) -> list[dict]:
    """
    Функция возвращает список со стоимостью каждой валюты по курсу на сегодня
    """
    rates = []
    try:
        for currency in rates_list:
            response = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY_RATES}/latest/{currency}")

            status_code = response.status_code
            exchange_rates_logger.info(f"Статус код запроса {status_code}")

            try:
                data = response.json()
                rates.append({"currency": currency, "rate": data["conversion_rates"]["RUB"]})
            except KeyError:
                exchange_rates_logger.error("keyerror")

        exchange_rates_logger.info("Запрос, стоимость валют")

        return rates
    except ExceptionGroup:
        exchange_rates_logger.warning("ошибка в запросе")
        return rates


def share_price(price: list) -> list[dict]:
    """Функция возврашает стоимость акций."""
    prices = []
    try:
        for stock in price:
            params = {
                "apikey": f"{API_KEY_RA}",
                "interval": "1day",
                "format": "JSON",
                "type": "stock",
                "symbol": f"{stock}",
                "outputsize": 1,
                "timezone": "Europe/Moscow",
            }

            response = requests.get("https://api.twelvedata.com/time_series", params=params)
            share_price_logger.info("запрос статус = 200")

            data = response.json()
            prices.append({"stock": stock, "price": data["values"][0]["close"]})
            return prices
    except ExceptionGroup:
        share_price_logger.warning("ошибка в запросе")


client = freecurrencyapi.Client(f"{API_KEY_RA}")
if __name__ == "__main__":
    exel_cashback = pd.read_excel("../data/operations.xlsx")
    exel_transaction = pd.read_excel("../data/operations.xlsx")
    exel_card = pd.read_excel("../data/operations.xlsx")
    exel_all_sum = pd.read_excel("../data/operations.xlsx")
    print(greetings_user())
    print(get_card_number_mask(exel_card))
    print(top_transaction(exel_transaction))
    print(get_exchange_rates(load_json["user_currencies"]))
    print(share_price(load_json["user_stocks"]))
