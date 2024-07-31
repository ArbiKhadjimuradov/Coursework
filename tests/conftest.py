import pytest


@pytest.fixture
def fixture_for_number():
    return [{'Дата операции': '18.11.2021 21:15:27', 'Дата платежа': '19.11.2021', 'Номер карты': 'Отсутствует',
             'Статус': 'OK', 'Сумма операции': -200.0, 'Валюта операции': 'RUB', 'Сумма платежа': -200.0,
             'Валюта платежа': 'RUB', 'Кэшбэк': 'Отсутствует', 'Категория': 'Мобильная связь', 'MCC': 'Отсутствует',
             'Описание': 'Тинькофф Мобайл +7 995 555-55-55', 'Бонусы (включая кэшбэк)': 2,
             'Округление на инвесткопилку': 0,
             'Сумма операции с округлением': 200.0}]


@pytest.fixture
def currency_usd():
    return {'currency': 'USD', 'rate': 88.1883}


@pytest.fixture
def currency_eur():
    return {'currency': 'EUR', 'rate': 96.2559}


@pytest.fixture
def stocks_aapl():
    return [{'stock': 'AAPL', 'price': '224.58350'}]


@pytest.fixture
def requests_aapl():
    return {
        'meta': {
            'symbol': 'AAPL',
            'interval': '1day',
            'currency': 'USD',
            'exchange_timezone': 'America/New_York',
            'exchange': 'NASDAQ',
            'mic_code': 'XNGS',
            'type': 'Common Stock'
        },
        'values':
            [
                {'datetime': '2024-07-19',
                 'open': '224.85201',
                 'high': '226.80000',
                 'low': '223.27499',
                 'close': '224.58350',
                 'volume': '34289484'
                 }
            ],
        'status': 'ok'
    }


@pytest.fixture
def result_fixture():
    return {'Yes': [50, 21], 'No': [131, 2]}


@pytest.fixture
def result_spending_by_category():
    return {
        'MCC': {},
        'Бонусы (включая кэшбэк)': {},
        'Валюта операции': {},
        'Валюта платежа': {},
        'Дата операции': {},
        'Дата платежа': {},
        'Категория': {},
        'Кэшбэк': {},
        'Номер карты': {},
        'Округление на инвесткопилку': {},
        'Описание': {},
        'Статус': {},
        'Сумма операции': {},
        'Сумма операции с округлением': {},
        'Сумма платежа': {}
    }

