metapdf
=======

Installation
------------

    easy_install metapdf

Usage
-----

```python
from metapdf.metapdf import MetaPdfReader
MetaPdfReader().read_metadata('1984.pdf')
```

    {
        Author: 'George Orwell',
        Title: '1984'
    }
