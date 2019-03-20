import subprocess
import threading
import signal
import time
import sys

DONT_KILL = 3

def main(arg):
    while True:
        time.sleep(1)
        print(f'Serving.')


def run_main(arg):
    while True:
        print(f'Spawning new process.')
        exit_code = subprocess.call(['python3', 'reloader.py', 'restart'], close_fds=False)
        if exit_code != DONT_KILL:
            return exit_code


def run_reloader():
    time.sleep(3)
    print('Found changes in file. Killing current subprocess.')
    sys.exit(DONT_KILL)


if __name__ == '__main__':
    arg = sys.argv[1:]
    if arg and arg[0] == 'restart':
        t = threading.Thread(target=main, args=[arg])
        t.setDaemon(True)
        t.start()
        run_reloader()
    else:
        sys.exit(run_main(arg))