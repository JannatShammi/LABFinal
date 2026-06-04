from id_calc import sum_of_odds_from_id


def test_valid_id_sequence():
    assert sum_of_odds_from_id("2022200000040") == 36


def test_empty_or_spaced_input():
    assert sum_of_odds_from_id("") == 0
    assert sum_of_odds_from_id("     ") == 0


def test_invalid_characters():
    assert sum_of_odds_from_id("2022A0000040") == 0