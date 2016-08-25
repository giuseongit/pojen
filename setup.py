from setuptools import setup, find_packages

setup(
    name = "Pojen",
    version = "0.1",
    packages = find_packages(),

    # metadata for upload to PyPI
    author = "Giuseppe Pagano",
    author_email = "giuseppe.pagano.p@gmail.com",
    description = "Generates POJO based on JSON structure",
    license = "MIT",
    keywords = "POJO java json mapper",
    url = "https://github.com/giuseongit/pojen",   # project home page
)