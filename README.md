# MurphyML
My machine learning study project

# Project setup

## Using Pyenv + Anaconda

### Install pyenv
``` brew install pyenv  ```

### Setup pyenv

Setup your ~/.zshrc or ~/.bash_profile depending on your shell. For detailed settings. Refer to following command.

```pyenv init```

### Check available anaconda versions
```pyenv install --list | grep anaconda```

### Install anaconda
```pyenv install anaconda3-5.3.1```


## Using venv

### Create venv

If you are using python with newer version than 3.3, you can create virtual environment by

```python3 -m venv```

### Activate VM

```source venv/bin/activate```


# Dependencies

All dependencies are described in requirements.in file.

To install dependencies, use following commands

``` pip install -r requirements.txt ```

## Generate requirements.txt file

First, install pip-tools

``` python -m pip install pip-tools ```

Specify requirements in requirements.in file. Then run following command to update requirements.txt.

``` pip-compile ```



# Tests

We use pytest for unit testing. Use following commands to run tests.

``` 
pytest # run all tests.
pytest test # run all tests in specific package.
pytest test/sample_test.py # run tests in specific module.
pytest test/sample_test.py -k test_sample # run specific test case.
pytest test/sample_test.py::SampleTest::test_sample # run specific test case.
```


# ML Framework

We used Pytorch for ML research. 

https://github.com/pytorch/pytorch

