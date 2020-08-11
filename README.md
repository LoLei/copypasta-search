# copypasta-search

Search and retrieve copypasta on Reddit with Python

## Installation
```
pip install copypasta-search
```

## Usage
### Command line
```
$ python copypasta-search --help
usage: copypasta-search [-h] [-s] [--version] query

positional arguments:
  query       search term

optional arguments:
  -h, --help  show this help message and exit
  -s, --show  print output to stdout
  --version   show program's version number and exit
```

### Python module
```python
import copypasta_search as cps

# To store the pasta:
pasta = cps.get_copypasta('interject')
print(pasta)

# Or for direct output to stdout:
cps.get_copypasta('interject', print_pasta=True)
```