import pandas as pd
from src.views import views
from src.utils import get_card_number_mask, greetings_user, get_exchange_rates, share_price, top_transaction, load_json
from src.read_file import read_excel_file, read_defolt_exel
from src.services import filter_numbers
from src.reports import spending_by_category
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent

# def main():
#     user_input = input(f"Введите дату для поиска информации в формате дд.мм.гггг")
#     output = views(f"{user_input}")
#     return json.dumps(output, ensure_ascii=False, indent=3)


exel_transaction = pd.read_excel("../data/operations.xlsx")
exel_card = pd.read_excel("../data/operations.xlsx")
exel_all_sum = pd.read_excel("../data/operations.xlsx")
operation = read_excel_file("../data/operations.xlsx")
result = spending_by_category(read_defolt_exel(str(ROOT_PATH) + "../data/operations.xlsx"), "Аптеки")
if __name__ == "__main__":
    print(views("20.10.2022"))
    print(greetings_user())
    print(get_card_number_mask(exel_card))
    print(top_transaction(exel_transaction))
    print(get_exchange_rates(load_json["user_currencies"]))
    print(share_price(load_json["user_stocks"]))
    print(filter_numbers(operation))
    print(result)