
from setuptools import setup, find_packages

setup(
    name='mynotes',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'notes=mynotes:main',
        ],
    },
    install_requires=[
        'bcrypt',
        "psycopg2",
    ],
    classifiers=[
        'Programming Language :: Pzython :: 3',
    ],
    author='Ibrahim Oluwadurotimi',
    author_email='ibrahimdurotimi1@gmail.com',
    description='A command-line notes application with online storage capacity.',
    long_description='A command-line notes application with with online storage capacity.',
    url='https://github.com/Durotimi08/mynotes',
    license='MIT',
)
