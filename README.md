# muttlib 🐶📚

[![pipeline status](https://gitlab.com/mutt_data/muttlib/badges/master/pipeline.svg)](https://gitlab.com/mutt_data/muttlib/-/commits/master)[![coverage report](https://gitlab.com/mutt_data/muttlib/badges/master/coverage.svg)](https://gitlab.com/mutt_data/muttlib/-/commits/master)

## Description

Library with helper code to start a project by [Mutt Data](https://muttdata.ai/).

Current modules:

- `dbconn`: Somewhat homogeneus lib to access multiple DBs.
- `file_processing`: Helpers for concurrent file processing.
- `forecast`: Provides FBProphet a common interface to Sklearn and general
  utilities for forecasting problems, allowing wider and easier grid search for
  hyperparameters.
- `utils`: A single version of miscellaneous functions needed every now and then.
- `ipynb_const` and `ipynb_utils`: Utilities when doing exploratory work (helpful for jupyter notebooks).
- `gsheetsconn`: Module to make data interactions to/from Google Sheets <> Pandas.
- `gcd`: (Greatest Common Divisor, for lack of a better name - Ty @memeplex) Classes, abstract objects and other gimmicks.

## Table of Contents

- Installation
- Usage
- Contributing
- Development Setup
- Testing
- Code of Conduct
- Credits
- License

## Installation

Base lib:

```bash
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib
```

Parquet and Feather support:

```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[pyarrow]
```

IPython utils:

```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ipynb-utils]
```

Forecast:

```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[forecast]
```

Misc DB support for dbconn:
```
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[oracle]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[hive]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[postgres]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[mysql]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[sqlserver]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[moongo]
pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ibis]
```

Install custom branch:
```
pip install -e git+https://gitlab.com/mutt_data/muttlib.git@AWESOME_FEATURE_BRANCH#egg=muttlib
```

### Dirty Dry-run (done dirt cheap)

```bash
pip install -e git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib

python -c 'from muttlib import dbconn, utils'

pip install git+https://gitlab.com/mutt_data/muttlib.git#egg=muttlib[ipynb-utils]
python -c 'from muttlib import ipynb_const, ipynb_utils'
```

## Usage

###  Google Sheets Credentials

To use the client in `gsheetsconn.py` one must first get the appropriate credentials in Json format. These are provided by GCP (Google's computing platform - cloud).
**Important note**: to obtain the necessary credentials, one must first have a valid GCP account which implies that billing for that account is already enabled. Having a standalone @gmail.com email will generally not suffice. This reference may probably help: [on billing and accounts support for GCP](https://cloud.google.com/support/billing/).


A good and simple step by step guide on how to get the Json file credentials can be seen in this [medium post](https://medium.com/@denisluiz/python-with-google-sheets-service-account-step-by-step-8f74c26ed28e). These credentials will be used by our client to read/write/edit files in Google Sheets.

The general idea is that in GCP we need to create or use an existing project, then enable the Sheets and Drive APIs for the selected project and finally create new service-account credentials for your script. Download them in Json format and put them somewhere accessible to your script.
There are other types of credentials but in this way we can have a server-side script that does not require explicit user consent to proceed with auth.

## Contributing

### How to submit issues, bugs, security issues

<merge !64 MR>

### How to send PRs

### Documentation style

muttlib uses [Sphinx](https://www.sphinx-doc.org/en/master/) to autogenerate it's docs from docstrings. Pushing all the docs is too cumbersome. You can generate them locally like so:

```bash
pip install .[dev]
cd docs
make html
```

And open `docs/build/html/index.html` on your browser of choice.

Alternatively you can see the docs for the `master` branch [here.](https://mutt_data.gitlab.io/muttlib/index.html)


## Development Setup

### Pre-Commit for Version Control Integration

When developing you'll have to use the python library
[pre-commit](https://pre-commit.com/) to run a series of linters and formatters, defined
in `.pre-commit-config.yaml`, on each staged file.  There are two ways to install these
binaries:

### Global install of binaries

The easiest way to set this up is by first installing `pipx` with

```bash
pip3 install --user pipx
pipx ensurepath
```

and then use `pipx` to actually install the `pre-commit` binary along the linters and
formatters globally:

```bash
pipx install pre-commit --verbose
pipx install flake8 --spec git+https://github.com/PyCQA/flake8 --verbose
pipx inject flake8 flake8-bugbear flake8-docstrings --verbose
pipx install black --verbose
pipx install mypy --verbose
pipx install pylint --verbose
```

Once that's done, `cd` into the repo where `.pre-commit-config.yaml` exists, run
`pre-commit install` and you are good to go: every time you do a `git commit` it will run
the `pre-commit` hooks defined in `.pre-commit-config.yaml`. You can also install a pre-push hook with `pre-commit install -t pre-push`, which will additionally run all pytest tests before pushing.

### Local install of binaries

The binaries are also listed as `dev` packages in `setup.py`. Therefore you can
alternatively install `muttlib` locally in a virtual environment using `pipenv`. To do
that first clone the repo, `cd` into this `muttlib` folder and then run

```bash
pipenv install -e .[dev] --skip-lock
```

Since the `.pre-commit-config.yaml` forces `pre-commit` to execute the environment of the
shell at the time of `git commit` you'll then have to run `git commit` from within a
`pipenv` subshell by first running `pipenv shell`.


### CI jobs

By default, when creating new merge-requests to this lib, gitlab will spawn a
CI job for every push done to the remote branch. This will install muttlib in a
gitlab-provided docker-env that'll install all the extras specified in the
`.gitlab-ci.yml` file.

Then, the CI jobs will run a `setup.py test` for every push. If one test fails
then that merge request's merge option will be disabled.
**Note**: If your commit message contains [ci skip] or [skip ci], without
capitalization, the job will be skipped i.e. no CI job will be spawned for that
push.

Alternatively, one can pass the ci.skip Git push option if using Git 2.10 or newer: `git push -o ci.skip`
more info in https://docs.gitlab.com/ce/ci/yaml/README.html#skipping-builds.
`IMPORTANT`. If you skip the CI job it will not disable the option to do merge, be careful doing this.

**Important note on coverage:** A regex that captures the otuput from `pytest-cov` has been set from Settings -> CI/CD -> General Pipelines -> Test coverage parsing

**Important note**: the service-account credentials will effectively provide us with a google-valid email, whicih will act as the "user" editing/modifying/etc. the data in Google Sheets. This implies that this service email needs to have sufficient permissions to actually edit these files. In general, giving permissions to the needed sheets will suffice.

## Testing
Run all tests:
```
python setup.py test
```
Note: Some extra deps might be needed. Those can be added with this `pip install -e .[ipynb-utils]`.

Run all tests locally as CI:
```
gitlab-runner exec docker test
```
Note: This requires to install [gitlab-runner](https://docs.gitlab.com/runner/install/) (but not register) and docker.

Run coverage:
```
py.test --cov-report html:cov_html --tb=short -q --cov-report term-missing --cov=. test/
```

That should output a short summary and generate a dir `cov_html/` with a detailed HTML report that can be viewed by opening `index.html` in your browser.

## Code of Conduct
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## Credits
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

## License
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.