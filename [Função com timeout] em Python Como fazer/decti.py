import subprocess
from ofenaus import ofen_aus, sleep
from threading import Lock


def bobagem():
    x = 1
    y = 2
    while x < y:
        print("oi")
        sleep(0.5)


def subprocess_ping():
    pp = subprocess.Popen("ping -t 8.8.8.8")
    while True:
        print(pp)
        sleep(1)


@ofen_aus(timeout=3, print_debug=True, print_exceptions=True)
def thread_lock_aquire():
    my_lock = Lock()
    my_lock.acquire()
    my_lock.acquire()
    while True:
        print("test aquire")
        sleep(1)


if __name__ == "__main__":
    thread_lock_aquire()
