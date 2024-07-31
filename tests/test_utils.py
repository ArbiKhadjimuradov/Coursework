import pytest

from src.utils import get_exchange_rates, share_price
from unittest.mock import patch


@patch('requests.get')
def test_get_currency_rates_usd(mock_get, currency_usd):
    mock_get.return_value.json.return_value = currency_usd
    list_currency = ['USD']
    assert get_exchange_rates(list_currency) == []


@patch('requests.get')
def test_get_currency_rates_eur(mock_get, currency_eur):
    mock_get.return_value.json.return_value = currency_eur
    list_currency = ["EUR"]
    assert get_exchange_rates(list_currency) == []


@patch('requests.get')
def test_share_price(mock_get, stocks_aapl, requests_aapl):
    mock_get.return_value.json.return_value = requests_aapl
    list_currency = ["AAPL"]
    assert share_price(list_currency) == stocks_aapl