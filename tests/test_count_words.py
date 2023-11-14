from lib.count_words import *
def test_count_words():
    length_of_result = count_words('Makers')
    assert length_of_result == 6