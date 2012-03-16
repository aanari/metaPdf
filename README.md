metapdf
=======

The metapdf library is a lightweight Python library optimized for metadata extraction and insertion, and it is a fast wrapper over the excellent [pyPdf](https://github.com/mfenniak/pyPdf) library.  It works by quickly searching the last 2048 bytes of the PDF before parsing the xref table, offering a 50-60% performance increase over directly parsing the table line by line.


Installation
------------

    easy_install metapdf


Usage
-----

```python
>>> import os
>>> from metapdf import MetaPdfReader
>>> MetaPdfReader().read_metadata(read('1984.pdf', 'rb'))
{
    Author: 'George Orwell',
    Title: '1984'
}
```


License (MIT)
-------------

Copyright (c) 2012 Ali Anari

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
