import citeme

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4'
})
def my_func():
    return True
