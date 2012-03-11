#!/usr/bin/env python
from distutils.core import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()

setup(name= 'metaPdf',
      version='0.1',
      description='A lightweight PDF library optimized for metadata extraction and insertion',
      author='Ali Anari',
      author_email='ali@alianari.com',
      long_description=README,
      license='BSD',
      classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url='http://github.com/aanari/metaPdf',
      keywords='python pdf metadata extraction insertion',
      packages=[]
    )
