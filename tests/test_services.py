from src.services import filter_numbers


def test_filtering_by_number(fixture_for_number):
    assert filter_numbers(fixture_for_number)[0]["Описание"] == 'Тинькофф Мобайл +7 995 555-55-55'