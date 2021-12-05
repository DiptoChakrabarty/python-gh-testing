# python-gh-testing
![Build Status](https://github.com/DiptoChakrabarty/python-gh-testing/workflows/Python-Testing/badge.svg)

Repo to test python code with gh actions

## How to Setup
```sh

- Clone Repository
- Setup Virtualenv and Activate it
- Install Packages using pip and requirements.txt
- Run pytest -vv on the test directory to test 

```

## Files Present

- src/operation folder which contains main package 
    * addition.py : Simple addition function
    * BankCode.py : Create Classa Bank and add methods
- tests folder which has the tests for the package
    * test_operation.py : testing of opeartion.py file
    * test_bank.py : Testing of the bank class and its methods

## Configuration files

- tox.ini : Configuration for how tox tests should run
- setup.cfg : Configuration for the python package to be setup and installed
- pyproject.toml: Configuration for the pytest and mypy

## Install code as package
```sh
- The code is present in src/ folder
- To install that code as package use command ppip install -e .
```
