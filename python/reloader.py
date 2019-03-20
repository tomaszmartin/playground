import subprocess
import threading
import signal
import time
import sys


RELOAD = 3


def main(arg):
    while True:
        time.sleep(1)
        print(f'Serving.')


def run_main(arg):
    while True:
        print(f'Spawning new process.')
        exit_code = subprocess.call(['python3', 'reloader.py', 'restart'], close_fds=False)
        # If process returns exit RELOAD
        # Than spawn another subprocess
        # Else exit the app
        if exit_code != RELOAD:
            return exit_code


def run_reloader():
    time.sleep(3)
    print('Found changes in file. Killing current subprocess.')
    sys.exit(RELOAD)


if __name__ == '__main__':
    arg = sys.argv[1:]
    # Run the main loop only from subprocesses
    # not from the main process.
    # Wont be run at first launch.
    if arg and arg[0] == 'restart':
        t = threading.Thread(target=main, args=[arg])
        t.setDaemon(True)
        t.start()
        # Looking
        run_reloader()
    # At first launch start the loop that spawns
    # Subprocesses with current file.
    else:
        sys.exit(run_main(arg))