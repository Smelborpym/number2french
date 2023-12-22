from setuptools import setup, find_packages

setup(
    name="number2french",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'number2french=src.convert:main',
        ],
    },
    install_requires=[
        'click',
        'pandas'
    ],
)
