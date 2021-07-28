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

### Install pytorch

``` pip3 install torch torchvision torchaudio```



# ML Framework

We used Pytocrch for ML research. 

https://github.com/pytorch/pytorch

