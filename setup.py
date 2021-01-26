#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Tue Jan 26 21:20:26 CET 2021
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

from setuptools import setup, find_packages

setup(
    name="comporttest",
    version="xx.xx.xx",
    description="Simple reminder-training example : comporttest",
    author="Leonid Burmistrov",
    packages=find_packages(exclude=['etc','example-project']),
    long_description=description,
)
