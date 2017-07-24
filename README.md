# Citeme

Citeme is a package to easily add citations to your code similar to bibtex
citations. Using decorators on your functions and classes a library of
citations is built when those functions and classes are used.

At the end of your script you can output the citations to a bibtex file,
html or plain text

## Example
```python
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

my_func()

citeme.CiteMe().print_references()

>>> article my_handle {'volume': '4', 'author': 'Johnny Awesome', 'journal': 'Acme Journal on Cartoon Properties', 'title': 'A short guide to being awesome', 'year': '2017'}
```