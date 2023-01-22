from TinyTinyDebugger import (
function_debug,
detailed_debugger
)

@function_debug(
sleep_between_each_line=1)
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        print('r bigger n')
    indices = list(range(r))
    # provoking an Exception
    wrong = indices / 0
    return indices
combinations("ABCD", 2)
from pprint import pprint






@function_debug(
    active=True,  # used to disable the debugger
    write_log_file=False,  # if True, data will be saved to hdd. Import allow_long_path_windows from windows_filepath and execute before! function_debug won't check for path length, so it is better to allow long file names
    log_folder='c:\\debugmyfunction',  # default value is the folder "_tinytinydebugger_log" in cwd
    pause_for_n_seconds_when_except=10,  # Only important if continue_on_exceptions is True. The execution will be paused and you can read the Exception. When you are done, press ctrl+c to continue
    continue_on_exceptions=True,  # if True, the execution will go on
    capture_local_vars=True,  # If True, all local variables in the function will be saved after each line in: detailed_debugger.local_function_vars
    color_print=True,  # black/white or colored
    print_line=True,  # If False, the event "line" won't be printed
    print_return=True,  # If False, the event "return" won't be printed
    print_exception=True,  # If False, the event "exception" won't be printed
    print_execution_time=True,  # enable/disable printing of execution time
    print_local_vars=True,  # if True: prints all local variables in the function each line
    sleep_between_each_line=0,  # sleep after each line of code
)
def baba(x):
    print(4/x)

baba(10)
pprint(detailed_debugger
       .local_function_vars)
