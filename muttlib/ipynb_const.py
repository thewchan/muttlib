"""Constants for ipython exploratory notebooks."""
import numpy as np
import pandas as pd
from pandas.tseries import offsets

# SQL
COUNTRY_NAME = "ARGENTINA"
COUNTRY_ISO3 = "ARG"
MAIN_SAMPLE_PCT = 0.1
LIMIT_N = 30000
MB_TO_B_FACTOR = 1024*1024
SQL_DESCRIBE_QUERY = "SELECT TOP 1 * FROM {d}.{t}"
GET_COLUMNS_DESCRIPTIONS = """
  SELECT
      COLUMN_NAME,
      DATA_TYPE,
      IS_NULLABLE
      DATETIME_PRECISION
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE 
       TABLE_NAME = '{table}'
       AND TABLE_CATALOG = '{catalog}'
       """

# STATS
PERCENTILES = np.asarray([0.01, 0.03, 0.05, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5])
PERCENTILES = np.concatenate([PERCENTILES, (1 - PERCENTILES[::-1])[1:]])

# TIME
# # Because of data loss, we know < 19/03 we'll have bad data
START_DATE = pd.to_datetime('2018-10-01', dayfirst=False)
END_DATE = pd.datetime.now()
LAST_WEEK_DATE = END_DATE - pd.Timedelta('7d')
# # First day of a fixed month date of analysis
FIXED_MONTH_DATE = pd.to_datetime('2018-11-01', dayfirst=False)
HOURS_PER_DAY = 24

FRIENDS_DAY = pd.to_datetime(
    f'{pd.datetime.now().year}-07-20', dayfirst=False)

august_first = pd.to_datetime(
    f'{pd.datetime.now().year}-08-01', dayfirst=False)
kids_dow_iteration = 3  # third sunday each August
KIDS_DAY = pd.date_range(
    start=august_first, end=august_first + offsets.Day(21),
    freq='W-SUN')[kids_dow_iteration - 1]

october_first = august_first + offsets.MonthBegin(2)
mother_dow_iteration = 3  # third sunday each October
MOTHERS_DAY = pd.date_range(
    start=october_first, end=october_first + offsets.Day(21),
    freq='W-SUN')[mother_dow_iteration - 1]

june_first = august_first - offsets.MonthBegin(2)
father_dow_iteration = 3  # third sunday each June
FATHERS_DAY = pd.date_range(
    start=june_first, end=june_first + offsets.Day(21),
    freq='W-SUN')[father_dow_iteration - 1]
