# muttlib 🐶📚

Library with helper code to start a project by [Mutt Data](https://muttdata.ai/).

Current modules:

- `dbconn`: Somewhat homogeneus lib to access multiple DBs.
- `file_processing`: Helpers for concurrent file processing.
- `utils`: A single version of miscellaneous functions needed every now and then.
- `ipynb_const.py` and `ipynb_utils.py`: Utilities when for exploratory work.

## Install

Base lib:

```commandline
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib
```

IPython utils:

```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ipynb-utils]
```

Misc DB suppoort for dbconn:
```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[oracle]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[hive]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[postgres]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[sqlserver]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[moongo]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ibis]
```

Install custom branch:
```
pip install -e git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib@AWESOME_FEATURE_BRANCH
```

# Testing
Run all tests:
```
python setup.py test
```
Note: Some extra deps might be needed. Those can be added with this `pip install -e .[ipynb-utils]`.

Run coverage:
```
py.test --cov-report html:cov_html --tb=short -q --cov-report term-missing --cov=. test/
```

That should output a short summary and generate a dir `cov_html/` with a detailed HTML report that can be viewed by opening `index.html` in your browser.


## Dirty Dry-run (done dirt cheap)
```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib
=======

```commandline
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ipynb-utils]
```

Misc DB support for dbconn:

```commandline
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[oracle]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[hive]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[postgres]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[sqlserver]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[moongo]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ibis]
```

## Dirty Dry-run (done dirt cheap)

```commandline
pip install -e git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib

python -c 'from muttlib import dbconn, utils'

pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ipynb-utils]
python -c 'from muttlib import ipynb_const, ipynb_utils'
```

## Pre-Commit for Version Control Integration

When developing you'll have to use the python library
[pre-commit](https://pre-commit.com/) to run a series of linters and formatters, defined
in `.pre-commit-config.yaml`, on each staged file.  There are two ways to install these
binaries:

### Global install of binaries

The easiest way to set this up is by first installing `pipx` with

```commandline
pip3 install --user pipx
pipx ensurepath
```

and then use `pipx` to actually install the `pre-commit` binary along the linters and
formatters globally:

```commandline
pipx install pre-commit --verbose
pipx install flake8 --spec git+https://github.com/PyCQA/flake8 --verbose
pipx inject flake8 flake8-bugbear flake8-docstrings --verbose
pipx install black --verbose
pipx install mypy --verbose
pipx install pylint --verbose
```

Once that's done, `cd` into the repo where `.pre-commit-config.yaml` exists, run
`pre-commit install` and you are good to go: every time you do a `git commit` it will run
the `pre-commit` hooks defined in `.pre-commit-config.yaml`.

### Local install of binaries

The binaries are also listed as `dev` packages in `setup.py`. Therefore you can
alternatively install `muttlib` locally in a virtual environment using `pipenv`. To do
that first clone the repo, `cd` into this `muttlib` folder and then run

```commandline
pipenv install -e .[dev] --skip-lock
```

Since the `.pre-commit-config.yaml` forces `pre-commit` to execute the environment of the
shell at the time of `git commit` you'll then have to run `git commit` from within a
`pipenv` subshell by first running `pipenv shell`.


### CI jobs
The CI Jobs will run all the tests in the test dir for every push you make and if it fail it will disable the option to make a merge of that branch. 
If your commit message contains [ci skip] or [skip ci], using any capitalization, the commit will be created but the pipeline will be skipped.

Alternatively, one can pass the ci.skip Git push option if using Git 2.10 or newer:

git push -o ci.skip
more info in https://docs.gitlab.com/ce/ci/yaml/README.html#skipping-builds
`IMPORTANT`. If you skip the CI job it will not disable the option to do merge, be careful doing this.