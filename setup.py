from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README').read()


setup(name='segment_tree',
      version='0.2.1',
      description='The most comprehensive implementation of Segment Tree.',
      long_description=long_description,
      url='https://github.com/evgeth/segment_tree',
      author='Evgeny Yurtaev',
      author_email='eugene@yurtaev.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      keywords='segment, tree, range, rmq',
      python_requires='>=3')
