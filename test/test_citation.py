import citeme
import pytest

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4'
})
def my_func():
    return True

def test_citation():
    my_func()

    assert len(citeme.CiteMe().references) > 0

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4',
    'non-existant': 'this field does not exist'
})
def my_func_bad():
    return True

def test_bad_citation():
    citeme.set_pedantic(True)

    with pytest.raises(Exception):
        my_func_bad()
