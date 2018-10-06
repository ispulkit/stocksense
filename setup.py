
from setuptools import setup, find_packages
from stocksense.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='stocksense',
    version=VERSION,
    description='Performs the magic of stock analysis',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Pulkit Kumar',
    author_email='ispulkitkr@gmail.com',
    url='https://github.com/ispulkit',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'stocksense': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        stocksense = stocksense.main:main
    """,
)
