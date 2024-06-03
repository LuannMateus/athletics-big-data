from setuptools import setup, find_packages

setup(
    name = 'athletics-big-data',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'streamlit',
        'pandas',
        'matplotlib',
        'playwright',
        'scrapy',
    ],
    entry_points = {
        'console_scripts': [],
    },
    author = 'LuannMateus',
    description = '',
    url = 'https://github.com/LuannMateus/athletics-big-data',
)
