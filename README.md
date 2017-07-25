# Citeme

Citeme is a package to easily add citations to your code similar to bibtex
citations. Using decorators on your functions and classes a library of
citations is built when those functions and classes are used.

At the end of your script you can output the citations to a bibtex file,
html or plain text

## Example

### Writing to a bibtex file
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

# Calling the function will add the citation to the
# library
my_func()

# Write all the citations to a bibtex file
write_to_bibtex('called.bib')
```

### Terminal Output
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

# Calling the function will add the citation to the
# library
my_func()

# Write the citations to the standard out
citeme.print_references()

# Example output
>>> article my_handle {'volume': '4', 'author': 'Johnny Awesome', 'journal': 'Acme Journal on Cartoon Properties', 'title': 'A short guide to being awesome', 'year': '2017'}
```