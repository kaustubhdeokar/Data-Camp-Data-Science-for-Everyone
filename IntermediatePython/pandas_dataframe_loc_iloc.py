Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data = pd.read_csv('./home/kaustubh/Desktop/brics.csv')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data = pd.read_csv('./home/kaustubh/Desktop/brics.csv')
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/io/parsers.py", line 688, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/io/parsers.py", line 454, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/io/parsers.py", line 948, in __init__
    self._make_engine(self.engine)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/io/parsers.py", line 1180, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/io/parsers.py", line 2010, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 382, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 674, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] No such file or directory: './home/kaustubh/Desktop/brics.csv'
>>> "f387eded3fa4ddc3104b7775e62d59065b30205c2758a8b86b4c27144adafcc4"=="f387eded3fa4ddc3104b7775e62d59065b30205c2758a8b86b4c27144adafcc4"
True
>>> data=pd.read_csv('./brics.csv')
>>> data
  Unnamed: 0       country    capital    area  population
0         BR        Brazil   Brasilia   8.516      200.40
1         RU        Russia     Moscow  17.100      143.50
2         IN         India  New Delhi   3.286     1252.00
3         CH         China    Beijing   9.597     1357.00
4         SA  South Africa   Pretoria   1.221       52.98
>>> print(data,index_col=0)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(data,index_col=0)
TypeError: 'index_col' is an invalid keyword argument for print()
>>> data['country']
0          Brazil
1          Russia
2           India
3           China
4    South Africa
Name: country, dtype: object
>>> data[['country
      
SyntaxError: EOL while scanning string literal
>>> data[['country'],['capital']]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data[['country'],['capital']]
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 2906, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2898, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 70, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 75, in pandas._libs.index.IndexEngine.get_loc
TypeError: '(['country'], ['capital'])' is an invalid key
>>> data[['country','capital']]
        country    capital
0        Brazil   Brasilia
1        Russia     Moscow
2         India  New Delhi
3         China    Beijing
4  South Africa   Pretoria
>>> 
>>> data[0:3]
  Unnamed: 0 country    capital    area  population
0         BR  Brazil   Brasilia   8.516       200.4
1         RU  Russia     Moscow  17.100       143.5
2         IN   India  New Delhi   3.286      1252.0
>>> data.loc["BR"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data.loc["BR"]
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexing.py", line 879, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexing.py", line 1110, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexing.py", line 1059, in _get_label
    return self.obj.xs(label, axis=axis)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/generic.py", line 3493, in xs
    loc = self.index.get_loc(key)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexes/range.py", line 358, in get_loc
    raise KeyError(key)
KeyError: 'BR'
>>> datadata=pd.read_csv('./brics.csv',index_col=0)
>>> data=pd.read_csv('./brics.csv',index_col=0)
>>> data
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Delhi   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98
>>> data.loc["BR"]
country         Brazil
capital       Brasilia
area             8.516
population       200.4
Name: BR, dtype: object
>>> data.loc[["BR"]]
   country   capital   area  population
BR  Brazil  Brasilia  8.516       200.4
>>> data.loc[["BR","IN"]]
   country    capital   area  population
BR  Brazil   Brasilia  8.516       200.4
IN   India  New Delhi  3.286      1252.0
>>> data.loc[["BR","IN"]]
   country    capital   area  population
BR  Brazil   Brasilia  8.516       200.4
IN   India  New Delhi  3.286      1252.0
>>> data[-1][-1]
Traceback (most recent call last):
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2898, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 70, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 101, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1675, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1683, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: -1

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data[-1][-1]
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 2906, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2900, in get_loc
    raise KeyError(key) from err
KeyError: -1
>>> data.iloc[-1][-1]
52.98
>>> data
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Delhi   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98
>>> print(data.iloc[:,:])
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Delhi   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98
>>> print(data.iloc[:,2])
BR     8.516
RU    17.100
IN     3.286
CH     9.597
SA     1.221
Name: area, dtype: float64
>>> print(data.iloc[[:,2]])
SyntaxError: invalid syntax
>>> print(data.iloc[:],[2]])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> print(data.iloc[:],[2])
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Delhi   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98 [2]
>>> print(data.iloc[:,2)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(data.iloc[:,2])
BR     8.516
RU    17.100
IN     3.286
CH     9.597
SA     1.221
Name: area, dtype: float64
>>> type(data.iloc[:,:])
<class 'pandas.core.frame.DataFrame'>
>>> print(data.loc[:][:])
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Delhi   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98
>>> print(data.loc[:]['country'])
BR          Brazil
RU          Russia
IN           India
CH           China
SA    South Africa
Name: country, dtype: object
>>> print(data.loc[:]['country','capital'])
Traceback (most recent call last):
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2898, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 70, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 101, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1675, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1683, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('country', 'capital')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(data.loc[:]['country','capital'])
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/frame.py", line 2906, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/kaustubh/.local/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 2900, in get_loc
    raise KeyError(key) from err
KeyError: ('country', 'capital')
>>> print(data.loc[:][['country','capital']])
         country    capital
BR        Brazil   Brasilia
RU        Russia     Moscow
IN         India  New Delhi
CH         China    Beijing
SA  South Africa   Pretoria
>>> print(data.loc[:][['country','capital']])
         country    capital
BR        Brazil   Brasilia
RU        Russia     Moscow
IN         India  New Delhi
CH         China    Beijing
SA  South Africa   Pretoria
>>> 