from setuptools import setup
from setuptools import find_packages

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='segment_tree',
      version='0.1.1',
      description='The most comprehensive implementation of Segment Tree.',
      long_description=long_description,
      url='https://github.com/evgeth/segment_tree',
      author='Evgeny Yurtaev',
      author_email='eugene@yurtaev.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      keywords='sample setuptools development',
      python_requires='>=3')
