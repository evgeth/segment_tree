from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    print('hey')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(name='segment_tree',
      version='0.1.4',
      description='The most comprehensive implementation of Segment Tree.',
      long_description=long_description,
      url='https://github.com/evgeth/segment_tree',
      author='Evgeny Yurtaev',
      author_email='eugene@yurtaev.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      keywords='segment, tree, range, rmq',
      python_requires='>=3')
