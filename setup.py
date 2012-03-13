#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name= 'metaPdf',
      version='0.2.3',
      description='A lightweight PDF library optimized for metadata extraction and insertion',
      long_description='',
      author='Ali Anari',
      author_email='ali@alianari.com',
      license='BSD',
      zip_safe=True,
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
      url='https://github.com/aanari/metaPdf',
      keywords='python pdf metadata extraction insertion',
      packages=find_packages()
    )
