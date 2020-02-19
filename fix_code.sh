#!/usr/bin/env bash
echo "Collecting python files..."
py_files=$(git ls-files -- '*.py' ':!:*/docs/*.py')

echo "Running isort (autoformatter) in place..."
PIPENV_DONT_LOAD_ENV=1 pipenv run isort -m 3 -tc -q $py_files

echo "Running black (autoformatter) in place..."
PIPENV_DONT_LOAD_ENV=1 pipenv run black -l 79 -S -q $py_files

echo "Running flake8 (linter)..."
if ! PIPENV_DONT_LOAD_ENV=1 pipenv run flake8 $py_files; then
  echo "'flake8' returned non-zero code"
  exit 1
fi

echo "Running radon (Cyclomatic Complexity checker)..."
complex_files=$(PIPENV_DONT_LOAD_ENV=1 pipenv run radon cc -nc $py_files)
if [ "$complex_files" != "" ]; then
  echo "Please check these files for redundant complexity:"
  echo "$complex_files"
  exit 1
fi
