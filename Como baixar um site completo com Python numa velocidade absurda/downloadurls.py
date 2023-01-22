from site2hdd import download_url_list

urls = [r'''https://pandas.pydata.org/docs/#''', r'''https://pandas.pydata.org/docs/getting_started/index.html''',
       r'''https://pandas.pydata.org/docs/user_guide/index.html''',
       r'''https://pandas.pydata.org/docs/reference/index.html''',
       r'''https://pandas.pydata.org/docs/development/index.html''',
       r'''https://pandas.pydata.org/docs/whatsnew/index.html''', r'''https://pandas.pydata.org/docs/dev/index.html''',
       r'''https://pandas.pydata.org/docs/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.4/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.3/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.2/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.1/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.0/index.html''',
       r'''https://github.com/pandas-dev/pandas''', r'''https://twitter.com/pandas_dev''',
       r'''https://pandas.pydata.org/docs/#pandas-documentation''', r'''https://pandas.pydata.org/docs/pandas.zip''',
       r'''https://pandas.pydata.org/''', r'''https://pypi.org/project/pandas''',
       r'''https://github.com/pandas-dev/pandas/issues''', r'''https://stackoverflow.com/questions/tagged/pandas''',
       r'''https://groups.google.com/g/pydata''', r'''https://pandas.pydata.org/docs/#module-pandas''',
       r'''https://www.python.org/''',
       r'''https://pandas.pydata.org/docs/getting_started/index.html#getting-started''',
       r'''https://pandas.pydata.org/docs/user_guide/index.html#user-guide''',
       r'''https://pandas.pydata.org/docs/reference/index.html#api''',
       r'''https://pandas.pydata.org/docs/development/index.html#development''',
       r'''https://pandas.pydata.org/docs/_sources/index.rst.txt''', r'''https://numfocus.org/''',
       r'''https://www.ovhcloud.com/''', r'''http://sphinx-doc.org/''', ]

download_url_list(urls, ProxyPickleFile=r'c:\newfilepath\myproxiefile\proxy.pkl',
   # The file you created using the function: get_proxies
   SaveFolder='c:\\site2hdd_urltest2',  # where should the files be saved
   try_each_url_n_times=5,  # maximum retries for each url
   ProxyConfidenceLimit=2,
   # each link will be downloaded twice and then compared. If only one result is positive, it counts as a not successful download. But if     the ProxyConfidenceLimit is higher, then it will be accepted
   ThreadLimit=30,  # downloads at the same time
   RequestsTimeout=10,  # Timeout for requests
   ThreadTimeout=12,  # Should be a little higher than RequestsTimeout
   SleepAfterKillThread=0.1,  # Don't put 0.0 here - it will use too much CPU
   SleepAfterStartThread=0.1,  # Don't put 0.0 here - it will use too much CPU
   IgnoreExceptions=True, )