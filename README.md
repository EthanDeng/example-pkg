# Introduction

This repo is created for the illustration of the combination of customized python package source code and sphinx doc structure. 

## Features

Some of features of this package "porotype" are:

1. remove the word "module" from the rendered html.
2. clean structure of doc and source code.
3. easy to copy to create new package.
4. most importantly, it's based upon my sense of beauty.

## build method

You can build the sdist and whl with

```shell
python setup.py sdist bdist_wheel
```

or build them separately.


## install package

After downloading the whl or tar.zip file, you can install the sublimate package by

```shell
pip install sublimate-x.y.z.tar.gz
pip install sublimate-x.y.z-py3-none-any.whl
```

