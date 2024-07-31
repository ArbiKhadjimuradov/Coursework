from src.reports import spending_result, spending_by_category
import pandas as pd
import pytest


def test_spending_result(result_fixture):
    @spending_result()
    def test_dataframe():
        df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
        return df

    assert type(test_dataframe().to_dict()) == type(result_fixture)


def test_spending_by_category(result_spending_by_category):
    file_test = pd.read_excel("../data/test_operation.xlsx")
    assert spending_by_category(file_test, "Переводы").to_dict() == result_spending_by_category