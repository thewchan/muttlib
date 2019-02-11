
import setuptools
import muttlib

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="muttlib-mutt",
    version=muttlib.__version__,
    author="Mutt Data",
    author_email="pablo@muttdata.ai",
    description="Collection of helper modules by Mutt Data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-html",
    ],
    test_suite='test',
    install_requires=[
        "jinja2",
        "pandas",
        "progressbar",
        "pyarrow",
        "pyyaml",
        "sqlalchemy",
        "scipy",
    ],
    extras_require={
        'oracle': ["cx_Oracle"],
        'hive': ["pyhive"],
        'postgres': ["psycopg2"],
        'sqlserver': ["pymssql"],
        'mongo': ["pymongo"],
        'ibis': ["ibis"],
        'ipynb-utils': [
            "IPython",
            "jinja2",
            "jinjasql",
            "matplotlib",
            "numpy",
            "pandas",
            "seaborn",
            "tabulate",
        ],
    }
)
