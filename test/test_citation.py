import pytest
import citeme

from fixtures import my_func, my_func_bad

def test_citation():
    my_func()

    assert len(citeme.CiteMe().references) > 0

def test_bad_citation():
    citeme.set_pedantic(True)

    with pytest.raises(Exception):
        my_func_bad()
