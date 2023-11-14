from lib. make_snippet import *

def test_make_snippet():
    result = make_snippet("James")
    assert result == "James"


def test_make_snippet_1():
    result = make_snippet("James-Leigh")
    assert result == '...'