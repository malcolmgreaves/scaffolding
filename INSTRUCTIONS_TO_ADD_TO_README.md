
1. Create the `conda` managed environment and download all dependencies. Then activate the environment.

```
conda env create && source activate scaffolding
```

2. Next, build the project and create symlinks to the code in the Python environment:

```
python setup.py build && python setup.py develop
```


To verify proper environment creation & project installation, perform the following checks:

- run tests with `pytest`
- build project documentation with `TODO`
- run example programs (see the `Examples` section below!)

