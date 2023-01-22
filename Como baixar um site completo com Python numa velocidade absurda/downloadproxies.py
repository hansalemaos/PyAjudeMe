from site2hdd import download_url_list,get_proxies,download_webpage
xlsxfile,pklfile = get_proxies(
  save_path_proxies_all_filtered='c:\\newfilepath\\myproxiefile\\proxy', #  path doesn't have to exist, it will be created, last
 # part (proxy) is the name of the file - pkl and xlsx will be added
 # important: There will be 2 files, in this case: c:\\newfilepath\\myproxiefile\\proxy.pkl and c:\\newfilepath\\myproxiefile\\proxy.xlsx

  http_check_timeout=6, # if proxy can't connect within 4 seconds to wikipedia, it is invalid

  threads_httpcheck=30, # threads to check if the http connection is working

  threads_ping=80 ,  # before the http test, there is a ping test to check if the server exists

  silent=False, # show results when a working server has been found

  max_proxies_to_check=5000, # stops the search at 2000
)
print(xlsxfile)
print(pklfile)