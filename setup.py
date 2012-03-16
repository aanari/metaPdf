#!/usr/bin/env python
from setuptools import setup, find_packages

requires = ['pyPdf']

setup(name= 'metapdf',
      version='0.3.2',
      description='A lightweight PDF library optimized for metadata extraction and insertion',
      long_description='',
      author='Ali Anari',
      author_email='ali@alianari.com',
      license='MIT',
      zip_safe=True,
      classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      url='https://github.com/aanari/metapdf',
      keywords='python pdf metadata extraction insertion',
      packages=find_packages(),
      install_requires=requires,
      tests_requires=requires
    )
