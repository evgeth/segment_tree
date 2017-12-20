from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path

long_description = open('README').read()

setup(
    name='segment_tree',
    version='0.3.1',
    description='Multidimensional segment tree with ranges updates.',
    long_description=long_description,
    url='https://github.com/evgeth/segment_tree',
    author='Evgeny Yurtaev',
    author_email='eugene@yurtaev.com',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    keywords='segment, tree, range, rmq, multidimensional',
    python_requires='>=2.7')
